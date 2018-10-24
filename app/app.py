from datetime import date

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.api.v1 import create_blueprint_v1
from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):

    # 会迭代调用的方法
    # 当jsonify遇到不能序列化的对象的时候就会调用
    # 字符串 数字
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder


def registe_blueprint(app):
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def registe_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    registe_blueprint(app)
    registe_plugin(app)
    return app
