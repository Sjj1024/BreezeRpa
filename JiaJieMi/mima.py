from werkzeug.security import generate_password_hash

# 生成密码
hash = generate_password_hash('xiaobao')

from werkzeug.security import check_password_hash

# 检查密码
print(check_password_hash(hash, 'ereg'))
print(check_password_hash(hash, 'xiaobao'))
