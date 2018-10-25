from werkzeug.exceptions import HTTPException

from app.libs.error import APIException
from app import create_app
from app.libs.error_code import ServerError

app = create_app()


@app.errorhandler(Exception)  # flask 1.0 才有的
def framework_error(e):
    # APIException
    # HTTPException
    # Exception
    # AOP
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    if isinstance(e, Exception):
        if app.config['DEBUG']:
            raise e
            # return ServerError(msg=str(e))
        return ServerError()


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
