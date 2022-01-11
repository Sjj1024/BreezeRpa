import Crypto.PublicKey.RSA
import Crypto.Random

x = Crypto.PublicKey.RSA.generate(2048)
a = x.exportKey("PEM")  # 生成私钥
b = x.publickey().exportKey()  # 生成公钥
with open("private_key.pem", "wb") as x:
  x.write(a)
with open("public_key.pem", "wb") as x:
  x.write(b)


# 使用 Crypto.Random.new().read 伪随机数生成器
y = Crypto.PublicKey.RSA.generate(2048, Crypto.Random.new().read)
c = y.exportKey()  # 生成私钥
d = y.publickey().exportKey()  # 生成公钥
with open("private_key2.pem", "wb") as x:
  x.write(c)
with open("public_key2.pem", "wb") as x:
  x.write(d)
