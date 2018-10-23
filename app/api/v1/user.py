from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('/get')
def get_user():
    return 'I am ten'

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

