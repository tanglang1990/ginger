from collections import namedtuple

from flask import current_app, g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, \
    BadSignature, SignatureExpired

# flask-httpauth
# pip install flask-httpauth
from app.libs.error_code import AuthFailed

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'scope'])


@auth.verify_password
def verify_password(token, password):
    # token
    # return True
    # headers key:value
    # account  ten
    # password 123456
    # HTTPBasicAuth
    # key:Authorization
    # value:basic base64(ten@qq.com:123456)
    # 可通过python代码获取
    # >>> import base64
    # >>> base64.b64encode('ten:123456'.encode('ascii'))
    # b'dGVuOjEyMzQ1Ng=='
    # value:basic base64(token:)

    # HTTP协议
    # HTTPBasicAuth
    user_info = verify_auth_token(token)
    g.user = user_info  # 数据的传递
    return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)
    uid = data['uid']
    ac_type = data['type']
    return User(uid, ac_type, '')

    # 里面存有用户信息
    # 加密
    # 过期时间的
