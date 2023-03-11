import random
import re
import string


def obfuscate_js(js_code):
    # 删除注释
    js_code = re.sub(r"(/\*([\s\S]*?)\*/)|(//(.*)$)", "", js_code)

    # 将js代码分割成语句
    stmts = re.split(";(?=(?:(?:[^']*'){2})*[^']*$)", js_code)

    # 对每个语句进行混淆加密
    obfuscated = ""
    for stmt in stmts:
        # 生成一个随机的函数名
        func_name = ''.join(random.sample(string.ascii_lowercase, 6))
        # 将语句包装成一个匿名函数，并用随机函数名替换掉原始函数名
        obfuscated += "(function " + func_name + "(){" + stmt + "})();" + "\n"

    return obfuscated


if __name__ == '__main__':
    js_code = """
    function runoob() {
        console.log('Hello World!');
    }
    runoob();
    """
    res = obfuscate_js(js_code)
    print(res)
