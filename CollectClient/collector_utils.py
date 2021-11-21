from mdt_api_client.creds import ClientKeySecretCredentials
from mdt_collector.collector_api.api_client.manager_client import ManagerClient
from mdt_collector.collector_api.api_client.template_client import \
    TemplateClient


def get_collector_base_url():
    """collector 域名"""
    return "https://abc.agile.com.cn/public/api"


def get_base_credential():
    """petal task 公用 collector 账号"""
    return ClientKeySecretCredentials(
        "yajule",
        "823f2f0f6068452ab1d1e97cc292affd"
    )


def get_manager_client_base():
    return ManagerClient.from_credentials(credentials=get_base_credential(), base_url=get_collector_base_url())


def get_template_client_base(template_uuid: str) -> TemplateClient:
    return TemplateClient.from_credentials(credentials=get_base_credential(),
                                           base_url=get_collector_base_url(),
                                           template_uuid=template_uuid)