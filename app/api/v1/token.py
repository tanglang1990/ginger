from flask import current_app, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm

api = Redprint('token')


# post包含的数据比通过url传递的数据相对更加安全
# ?account=ten@qq.com&password=123456
@api.route('', methods=['POST'])
def get_token():
    # 根据用户名和密码得到的一个钥匙token,以后请求服务器的时候就只要用token就可以了
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify
    }

    # token 包含用户信息 加密 能够解密 有有效期
    expiration = current_app.config['TOKEN_EXPIRATION']
    identity = promise[form.type.data](
        form.account.data, form.secret.data)
    token = generate_auth_token(
        identity['uid'], form.type.data, None, expiration)
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None,
                        expiration=7200):
    '''生成令牌'''
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps(
        {
            'uid': uid,
            'type': ac_type.value
        }
    )
