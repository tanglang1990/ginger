from flask import current_app, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, TimedJSONWebSignatureSerializer, \
    SignatureExpired, BadSignature

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import AuthFailed
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, TokenForm

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
        identity['uid'], form.type.data, identity['scope'], expiration)
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


@api.route('/secret', methods=['POST'])
def get_token_info():
    """获取令牌信息"""
    # 前端得到token 怎么样判断是否有效
    form = TokenForm().validate_for_api()
    s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(form.token.data, return_header=True)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)

    r = {
        'scope': data[0]['scope'],
        'create_at': data[1]['iat'],
        'expire_in': data[1]['exp'],
        'uid': data[0]['uid']
    }
    return jsonify(r)


def generate_auth_token(uid, ac_type, scope=None,
                        expiration=7200):
    '''生成令牌'''
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps(
        {
            'uid': uid,
            'scope': scope,
            'type': ac_type.value
        }
    )
