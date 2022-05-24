from flask_script import Manager
# 添加命令行支持，后面还要数据库迁移等功能
from FlaskBooks.Info import *

# 创建的时候传递环境配置
app = creat_app("pro")
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
    # app.run(host="0.0.0.0", port=5000)
