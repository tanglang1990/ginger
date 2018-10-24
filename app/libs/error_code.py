from app.libs.error import APIException


class Success(APIException):
    # 200 201
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    # 204 状态码，返回之后不会带有body的内容
    code = 202
    error_code = -1


class ClientTypeError(APIException):
    # 400 401(未授权，密码错误) 403(禁止访问，没有权限)  404
    # 500
    # 200 201 204
    # 301（永久） http://www.baidu.com  https://www.baidu.com  302 (临时)
    code = 400
    error_code = 1006
    msg = 'client is invalid'


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found O__O...'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1005
