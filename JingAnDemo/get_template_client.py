from collector_api.api_client.manager_client import ManagerClient
from collector_api.api_client.template_client import TemplateClient
from mdt_api_client.creds import ClientKeySecretCredentials
from mdt_config import config_server


def get_collector_base_url():
  """collector 域名"""
  # return config_server.get('/global/internal_url/collector_public')
  return "https://jabm.jingan.gov.cn/public/api"


def get_base_credential():
  """petal task 公用 collector 账号"""
  # return ClientKeySecretCredentials(
  #     config_server.get('collector/account/jingan_v2/key'),
  #     config_server.get('collector/account/jingan_v2/secret'),
  # )
  return ClientKeySecretCredentials(
      "b0473bd7e75f40b986158057ad5a2fe2",
      "a2c883fbea68409d9b9d878a54dc44c4",
  )


def get_manager_client_base():
  return ManagerClient.from_credentials(credentials=get_base_credential(), base_url=get_collector_base_url())


def get_template_client_base(template_uuid: str) -> TemplateClient:
  return TemplateClient.from_credentials(credentials=get_base_credential(),
                                         base_url=get_collector_base_url(),
                                         template_uuid=template_uuid)