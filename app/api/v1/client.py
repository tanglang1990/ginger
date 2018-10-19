from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # 注册
    # 表单 json
    # request json response json
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        # 很多种不同的客户端
        # swith case
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_by_email
        }
    promise[form.type.data]()
    return 'success'


def __register_by_email():
    # User.register_by_email(, form.account.data, form.secret.data)

    data = request.json
    form = UserEmailForm(data=data)
    if form.validate():
        User.register_by_email(
            form.nickname.data,
            form.account.data,
            form.secret.data
        )

# HttpException
