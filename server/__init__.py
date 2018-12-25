from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def register_extensions(app: Flask):
    utility(app)

    from server import extensions

    extensions.cors.init_app(app)
    extensions.db.init_app(app)
    extensions.db.create_all(app=app)
    extensions.jwt.init_app(app)
    extensions.swagger.init_app(app)
    extensions.swagger.template = app.config['SWAGGER_TEMPLATE']


def utility(app: Flask):
    from server.view import Router

    Router(app).register()

    from server.config.config import Config

    app.config.from_object(Config)


def create_app():
    app = Flask(__name__)

    register_extensions(app)

    return app
