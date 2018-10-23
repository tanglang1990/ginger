from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.error_code import ClientTypeError
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # 我们可以接受定义的复杂，但是不能接受调用的复杂
    # 定义是一次的 调用是会重复n次的
    # 我们可以预知的异常 已知异常
    # 我们完全没有意识到的异常 未知异常
    # AOP
    # 1/0
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_by_email,
    }
    promise[form.type.data]()
    return Success()


def __register_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(
        form.nickname.data,
        form.account.data,
        form.secret.data
    )
