# coding=utf-8
from Utils import *
import time
import json

permissions = [
    # Permission.template_admin,
    # Permission.template_grant_permission,
    # 只读
    Permission.template_read,
    Permission.template_data_read,
    Permission.template_data_download,

    #
    # # # 文件上传
    # Permission.template_data_populate,
    # Permission.template_data_storage_read,
    # Permission.template_data_storage_create,
    # Permission.template_data_storage_delete,
    # Permission.template_data_storage_read_all,

    #
    # # # # # 数据增删改查
    Permission.template_data_create,
    Permission.template_data_update,
    Permission.template_data_batch_update,
    Permission.template_data_delete,
    Permission.template_data_batch_delete

    # # 模板结构
    # Permission.template_update,
]
if __name__ == '__main__':

    # 建表 表名
    title = '花木志愿者-热门搜索关键词'

    # 建表路径
    AuthApi.setEnvironment("production")
    path = "/Users/metrodata/workspace/document/建表相关/花木志愿者/【表结构】{}.xlsx".format(title)
    print(path)

    # 建表22
    uuid = Template.create_template_excel(path=path, title=title)

    # 复制表
    # uuid = 'e47dc5c9-7813-4f98-b726-ffd2b35eee75'
    Template(uuid).copy_template(copy_data=True, env_from='production', env_to='staging')
    print(uuid)

    # 开权限

    # uuid_list = PermissionManager.get_user_uuid(names=['徐纯',  '寸代永', '李海涵'])
    # huamu_sms = ['郑鑫禹', '谈思阅', '姚希茜', '寸代永', '李海涵', '海诗嘉',
    #              '赵一筱', '李鹏玺', '吴玄玉', '刘善壮']
    huamu_vol = ['李海涵', '曾亮', '陈怡含', '刘西慧', '谈思阅', '王朱恩', '钟华', '海诗嘉', '李俊杰',
                 '吴文邦', '郑怡青']
    # huamu_vol = ['李海涵', '王朱恩', '钟华', '李俊杰',
    #              '吴文邦', '郑怡青']
    uuid_list = PermissionManager.get_user_uuid(names=huamu_vol)
    # uuid_list = PermissionManager.get_user_uuid(names=['邹家唱'])
    for user_uuid in uuid_list:
        print(PermissionManager(uuid).operate_permission(user_uuid=user_uuid, permission=permissions))

    if AuthApi.environment == 'production':
        AuthApi.setEnvironment('staging')
    else:
        AuthApi.setEnvironment('production')

    uuid_list = PermissionManager.get_user_uuid(names=huamu_vol)
    for user_uuid in uuid_list:
        print(PermissionManager(uuid).operate_permission(user_uuid=user_uuid, permission=permissions))
    # 输出到飞书  仅用于花木项目
    default_content = {
        "shareToken": "shrcnX98at4aSXfSnAOPCCLCsUc",
        "data": "{{\"fldIYrgF4k\":{{\"type\":1,\"value\":[{{\"type\":\"text\",\"text\":\"{title}\"}}]}},\"fldl6PVC4n\":{{\"type\":1,\"value\":[{{\"type\":\"text\",\"text\":\"{uuid}\"}}]}},\"fldNWWf8lb\":{{\"type\":5,\"value\":{ts}}}}}".format(
            title=title, uuid=uuid, ts=str(int(time.time() * 1000)))
    }
    url = r'https://ivg5lkk1dw.feishu.cn/space/api/bitable/share/content'
    body = json.dumps(default_content, ensure_ascii=False)
    print(parse_url(url=url, payload=body.encode('utf-8')))
