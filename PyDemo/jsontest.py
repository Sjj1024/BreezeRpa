import json


list_str = '["a"]'
# list_str = "['abs', 'bsdf']"

list_a = json.loads(list_str)

print(list_a)