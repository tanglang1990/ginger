import sys
import os

cur_path = os.path.dirname(os.path.abspath(__file__))
rootPath = os.path.split(cur_path)[0]
print(rootPath)
sys.path.append(rootPath)
# # print(sys.path)
#
from app import create_app
from app.models.base import db
from app.models.user import User

# 如果直接通过工具添加数据到数据库的话，并不知道密码加密的值
app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建一个超级管理员
        user = User()
        user.nickname = 'admin5'
        user.password = '123456'
        user.email = 'admin5@qq.com'  # insert
        user.auth = 2
        db.session.add(user)
