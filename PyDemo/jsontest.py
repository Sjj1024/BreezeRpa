import json


list_str = '["a"]'
# list_str = "['abs', 'bsdf']"

list_a = json.loads(list_str)

print(list_a)


arr_list = ["a", "b", "c"]
res = "-".join(arr_list)

print(arr_list)