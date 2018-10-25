from app.api.v1 import create_blueprint_v1
from app.app import Flask


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