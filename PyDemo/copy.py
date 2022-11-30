import re
testStr = "www.a.com;www.b.c.d.com"


res = re.findall("www\.(.*?)\.com", testStr)

print(res)