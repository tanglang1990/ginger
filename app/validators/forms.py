from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, Email, Regexp, ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form



class ClientForm(Form):
    # 注册请求表单
    account = StringField(
        validators=[DataRequired(message='这个字段内容不能为空'), Length(
        min=5, max=32
    )])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    # type 命名是有问题的, 问题指风险，二进制

    def validate_type(self, field):
        try:
            client = ClientTypeEnum(field.data)
        except ValueError as e:
            raise ValidationError('客户端类型不合法')
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       Length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError('该邮箱对应的用户已注册')
