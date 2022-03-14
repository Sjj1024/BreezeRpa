import json


def test_json():
  dict_l = {'a': "1", 'b': None, 'c': 3, 'd': 4}
  if all(dict_l.values()):
    json_str = json.dumps(dict_l)
    print(json_str)


def list_demo():
  list_null = [""] * 4
  print(list_null)


if __name__ == '__main__':
  # test_json()
  list_demo()
