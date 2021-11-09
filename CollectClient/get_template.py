from collector_utils import *


def get_temp_man():
  data_manager = get_manager_client_base()
  lst = data_manager.template_list().keys()
  print(lst)


def get_temp_client():
  data_client = get_template_client_base("d175599c-7980-4bb4-b1c7-a7e5244f1e4a")
  print(data_client.template_extra())


if __name__ == '__main__':
  # get_temp_man()
  get_temp_client()
