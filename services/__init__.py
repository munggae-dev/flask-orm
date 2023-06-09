from flask import Flask, blueprints

import config
from models import db as _db

db = _db.db
migrate = _db.migrate

from . import admin


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(admin.app)
    from models import admin as admin_model

    return app
