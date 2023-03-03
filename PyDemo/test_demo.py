import re


def re_all():
    str_demo = """@com.txffp.api.core.manager.comm.annotation.Comment(describe="文件base64格式", required="是", rule=""), @javax.validation.constraints.NotBlank(message="文件base64格式不能为空")"""
    res = re.search(r'describe="(.*?)", required="(.*?)"', str_demo)
    print(res.group(0))
    print(res.group(1))
    print(res.group(2))


if __name__ == '__main__':
    re_all()
