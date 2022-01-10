try:
  import pytransform_bootstrap
except ImportError:
  pass

import json
from .utils.resources import Resources
from .exceptions import PluginIntentionalError


def update_data_table(_dbe, pro_template, data):
  """
  将更新数据同步到生产表里面
  """
  # 获取land_uuid，更新对应的记录
  land_uuid = data.get("land_uuid")
  _dbe.execute(f'UPDATE collector."data-{pro_template}" SET extra = '
               f"(extra::jsonb || '{json.dumps(data)}')"
               f"WHERE extra ->> 'land_uuid' = '{land_uuid}'")


class PluginsYajuleCheck:

  @staticmethod
  def pre_data_created(plugin_result, template_uuid: str, template_info: dict,
                       data: dict) -> dict:
    # 数据库引擎
    resources = Resources(template_uuid=template_uuid,
                          template_info=template_info)
    _dbe = resources.dbengine
    data = plugin_result or data
    # 获取目标表uuid
    pro_template = ""
    for each in template_info['extra']['plugins']:
      if 'customized' in each:
        pro_template = each['customized'].get('target_uuid')
    # 清除目标表的缓存，临时表会自动清理
    resources.clear_data_cache(template_uuid=pro_template)
    # 判断是跟新还是新增
    is_new = data.pop("is_new", False)
    if not is_new:
      # 更新部分字段
      update_data_table(_dbe, pro_template, data)
    return data
