from flask import jsonify, g

from app.libs.error_code import NotFound, DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Redprint('user')


class Ten:
    name = 'ten'
    age = 18

    def __init__(self):
        self.gender = 'male'

    def keys(self):
        return ['name', 'age']

    def __getitem__(self, item):
        return getattr(self, item)


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    # r = {
    #     'nickname': user.nickname,
    #     'email': user.email,
    # }
    # 追求更好的写法
    # 艺术 情怀
    # 编程的思路 线性的 容易
    # 抽象 很难
    # 枯燥？码农
    # 更好的写法，避免枯燥，让你有成就感
    # 业务 RESTFULL api

    # viewmodel
    # 内部开发
    # 1：普通用户 2： 管理员
    # 前端人员会更方便
    # user book

    # restfull api
    return jsonify(user)


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    # 1 1
    # 2 2
    uid = g.user.uid
    # g : 用来做数据传递的
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()

# 1.此处蓝图应该作为包级别的对象
# 2.url非常的冗余, /v1/user的部分非常多余


# blueprint
# redprint 红图


# RESTful API  设计规范

# 内部开发   外部api
# REST url 代表资源

# 前端会感觉吃力
# user books
# 1 接口粒度比较粗
# 2 HTTP请求次数大量增加
# 3 REST只是规范，可以借鉴，不一定要把它当成神话

# user -- User
# restful
# web app 小程序
# 客户端 client
# 种类非常多
# 注册形式非常多 邮箱 手机 微信公众号  小程序


# token 钥匙 1、加密的   2、有有效期的  3、解密的信息里面包含有用的信息
# 身份证
#  cookie
