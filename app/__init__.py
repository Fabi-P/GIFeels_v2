from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate
from authlib.integrations.flask_client import OAuth
from flask_bcrypt import Bcrypt
from app.settings.settings import Config
from flask_cors import CORS
from app.settings.cors_policy import cors_resource
from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()
oauth = OAuth()
bcrypt = Bcrypt()
limiter = Limiter(get_remote_address)
cors = CORS()
csrf = CSRFProtect()


def create_app(config_class=Config, test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_class)

    if test_config:
        app.config.update(test_config)

    app.jinja_env.lstrip_blocks = True

    app.jinja_env.trim_blocks = True

    db.init_app(app)
    oauth.init_app(app)
    bcrypt.init_app(app)
    limiter.init_app(app)
    cors.init_app(app, resources=cors_resource)
    csrf.init_app(app)

    Migrate(app, db)

    from app.routes import main

    app.register_blueprint(main)

    return app