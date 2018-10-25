from collections import namedtuple

from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, \
    BadSignature, SignatureExpired

# flask-httpauth
# pip install flask-httpauth
from app.libs.error_code import AuthFailed, Forbidden
from app.libs.scope import is_in_scope

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'is_admin'])


@auth.verify_password
def verify_password(token, password):
    user_info = verify_auth_token(token)
    g.user = user_info
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
    scope = data['scope']
    ac_type = data['type']

    # endpoint
    allow = is_in_scope(scope, request.endpoint)
    if not allow:
        raise Forbidden()

    return User(uid, ac_type, scope)

    # 里面存有用户信息
    # 加密
    # 过期时间的
