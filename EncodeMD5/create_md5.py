import hashlib

# import md5 #Python2里的引用
s = 'mdtdemo98f376267240491c9c7ce3d76e6910ff1562552864582c08bd48ad46f8abc5a95fb11f43e2'
# s.encode()#变成bytes类型才能加密
m = hashlib.md5(s.encode())
print(m.hexdigest())

# m = hashlib.sha3_224(s.encode())  # 长度是224
# print(m.hexdigest())
#
# m = hashlib.sha3_256(s.encode())  # 长度是256
# print(m.hexdigest())
#
# m = hashlib.sha3_512(s.encode())  # 长度是512
# print(m.hexdigest())
