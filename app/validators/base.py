from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        args = request.args.to_dict()
        data = request.get_json(silent=True)  # 静默处理，有异常也没不会抛出
        super(BaseForm, self).__init__(data=data, **args)

    def validate(self):
        # 定义一个父类有的方法，然后改造父类的方法
        pass

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        # 为了方便前端人员调试，我们返回的信息应该方便调试，而不是每次都来问
        # 后端人员现在怎么了
        # form errors
        if not valid:
            raise ParameterException(msg=self.errors)
        return self

