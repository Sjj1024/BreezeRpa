class Task(object):
  """任务

  任务是petal的最小调度单元
  """

  _params = {}

  @property
  def params(self):
    return self._params

  @params.setter
  def params(self, params):
    self._params = AttrDict(params)

  @property
  def context_kwargs(self):
    return self._context_kwargs

  @context_kwargs.setter
  def context_kwargs(self, context_kwargs):
    self._context_kwargs = AttrDict(context_kwargs)

  @property
  def g(self):
    return self.context_kwargs

  @property
  def p(self):
    return self.params

  @property
  def v(self):
    return self.vars

  def init(self):
    pass

  def __init__(self, limit=-1):
    self._datapkgs = []
    self._params = AttrDict({})

    if hasattr(self.__class__, 'meta'):
      logger_name = self.__class__.meta.id
    else:
      logger_name = self.__class__.__name__
    self.logger = getLogger(logger_name)
    # 为每个Instance都分配一个vars变量，提供一个统一的地方在Steps之间传递参数，
    # 而不是现在这样使用Task Attributes
    self.vars = AttrDict()

  @staticmethod
  def get_common_arg_parser(name: str='task'):
    return argutil.get_common_arg_parser(name)

  @staticmethod
  def get_cls_arg_parser(cls, *args, **kwargs) -> argparse.ArgumentParser:
    return argutil.get_cls_arg_parser(cls, *args, **kwargs)

  @classmethod
  def get_arg_parser(cls) -> argparse.ArgumentParser:
    return argutil.get_cls_arg_parser(cls)

  def _notify_data_pkg_change(self):
    if 'dbe' in self.v:
      dbe = self.v.dbe
    else:
      dbe = self.dbe
    for pkg in self._datapkgs:
      appid = pkg.get('appid', 0)
      if pkg['source'] in (DataSource.market, DataSource.customer):
        msg = {'source': pkg['source']}
        ids = pkg.get('ids')
        if ids is not None:
          msg['id'] = ids
        else:
          msg['uuid'] = dbe.pkg_name_to_uuid(source=pkg['source'],
                                             names=pkg['names'],
                                             appid=appid,
                                             geotype=pkg.get('geotype'))
      else:
        raise ValueError('Unknown data source %s' % pkg['source'])

      # workers does not support 0 value of app_id
      if appid != 0:
        msg['app_id'] = appid
      worker_client.get_client().notify_package_change(**msg)

  def on_success(self):
    """Task执行成功后的回调"""
    if getattr(self, '_datapkgs', None):
      if self.p.notify_worker:
        self._notify_data_pkg_change()
        self.logger.info('发送数据包更新通知并清理缓存')
      else:
        self.logger.warn('本次任务不发送更新通知,不清理缓存')

  def on_failure(self, err: Exception):
    """Task执行失败后的回调

    会传入Exception作为第一个参数，以便任务可以对Exception进行定制化处理。
    注意，在这个函数中无法抑制Exception的raise，因为无论如何，任务已经失败了。
    如果没有raise新的Exception，会raise原始的Exception
    """
    pass

  def on_finish(self):
    """Task执行完成后的回调（不论成功与否）"""
    pass

  @overload
  def new_etl(self, stream: Literal[False] = ...) -> ETL:
    ...

  @overload
  def new_etl(self, stream: Literal[True]) -> ETLStream:
    ...

  def new_etl(self, stream=False):
    """
    Args:
      stream (bool): 如果为True，返回ETLStream，使用流式ETL; 如果为False，使用
        常规ETL。
    """
    if stream:
      return ETLStream(options=ETLOptions(self.params), logger=self.logger)
    return ETL(options=ETLOptions(self.params), logger=self.logger)

  def bind_dbe(self, dbe: DBEngineX):
    """绑定一个DBEngineX"""
    self.dbe = dbe
    self.v.dbe = dbe
    return self

  def _bind_datapkg(self, pkg: dict):
    if not hasattr(self, '_datapkgs'):
      self._datapkgs = []
    self._datapkgs.append(pkg)
    return self

  def _bind_market_meta_pkg(self):
    # 强行绑定一次 数据市场数据包统计; 私有化部署可能不存在这个数据包
    if not getattr(self, '_meta_pkg_bound', False):
      try:
        self.logger.info('自动绑定数据市场统计数据包', id=MARKET_META_PKG_ID)
        self._bind_datapkg({
          'source': DataSource.market,
          'ids': [MARKET_META_PKG_ID],
        })
        setattr(self, '_meta_pkg_bound', True)
      except Exception as e:
        self.logger.warning(e.args[0])

  def bind_market_pkgs_by_name(self, names, *, appid: int = 0):
    """
    通过名称绑定若干市场数据包到Task， Task执行成功后会清除和该数据包相关的缓存

    Args:
      names: (list<str> or str): 一个或多个数据包名称
      appid: (int): 对于专享数据包，需要指定appid
    """
    # bind a data package, if a data package is bind to a task, after the
    # task finishes, all cache related this data package will be cleaned
    self.logger.info('通过名称绑定数据市场数据包', names=names, appid=appid)
    self._bind_market_meta_pkg()
    return self._bind_datapkg({
      'source': DataSource.market,
      'names': names,
      'appid': appid,
    })

  def bind_market_pkgs_by_id(self, ids):
    """
    通过id绑定若干市场数据包到Task， Task执行成功后会清除和该数据包相关的缓存

    Args:
      ids: (list<int> or int): 一个或多个数据包id
    """
    self.logger.info('通过id绑定数据市场数据包', ids=ids)
    self._bind_market_meta_pkg()
    return self._bind_datapkg({
      'source': DataSource.market,
      'ids': ids,
      'appid': None,
    })

  def bind_customer_pkgs_by_id(self, object_type_ids: list, appid: int):
    """
    通过id绑定若干私有数据包到Task， Task执行成功后会清除和该数据包相关的缓存

    Args:
      object_type_ids: (list<int> or int): 一个或多个数据包id
      appid: (int): 私有数据所属的app id
    """
    assert appid > 0
    self.logger.info('通过id绑定私有数据包', ids=object_type_ids, appid=appid)
    return self._bind_datapkg({
      'source': DataSource.customer,
      'ids': object_type_ids,
      'appid': appid,
    })

  def bind_customer_pkgs_by_name(self,
                                 names: list,
                                 *,
                                 appid: int,
                                 geotype: GeometryType = None):
    """
    通过名称绑定若干私有数据包到Task， Task执行成功后会清除和该数据包相关的缓存

    Args:
      names: (list<str> or str): 数据包名称
      appid: (int): 私有数据所属的app id
      geotype (GeometryType): 地理类型
    """
    assert appid > 0
    self.logger.info('通过名称绑定私有数据包', names=names, appid=appid, geotype=geotype)
    return self._bind_datapkg({
      'source': DataSource.customer,
      'names': names,
      'appid': appid,
      'geotype': geotype,
    })

  def run_subtask(self,
                  task_cls,
                  progress_quota=None,
                  progress_desc=None,
                  **kwargs):
    """
    运行子Task

    子Task需要从当前Task继承一些参数
    """
    kwargs['taskid'] = self.runtime.kwargs['taskid']
    kwargs['mode'] = self.runtime.kwargs['mode']
    for arg_name in ('limit', 'srs', 'encoding', 'silent'):
      if arg_name not in kwargs:
        kwargs[arg_name] = self.runtime.kwargs[arg_name]
    if progress_quota is None:
      quota_kwargs = {'quota_free_rate': 1.0}
    else:
      quota_kwargs = {'quota': progress_quota}
    kwargs['_progress'] = self.progress.start_milestone(
        **quota_kwargs,
        total=1.0,
        desc=progress_desc or task_cls.__name__)
    return run_task(task_cls, parent=self, **kwargs)