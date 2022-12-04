from jsonschema import validate


# 编写校验函数
def check_metadata(json_data, schema):
    """
    正确返回True 错误返回异常的日志
    """
    try:
        validate(instance=json_data, schema=schema)
        return True
    except Exception as e:
        return e


schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "Test",
    "description": "Check a test schema",
    "type": "object",
    "properties": {
        "email": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$"
        },
        "host": {
            "type": "integer",
        },
    },
    "required": [  # 必填字段
        "email",
        "host"
    ]
}

# json 校验结果
json_data1 = {"email": "1245010032@qq.com", "host": 123}  # 正确
json_data2 = {"email": "1245010032qq.com", "host": 123}  # 错误
json_data3 = {"email": "1245010032@qq.com", "host": "123"}  # 错误


if __name__ == '__main__':
    res = check_metadata(json_data3, schema)
    print(res)