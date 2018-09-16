#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask

from config import base_config
from app.auth import auth
from app.database import db
from flask_script import Manager
from flask_migrate import MigrateCommand
from lib.extensions import mail, migrate, bcrypt, rq


def create_rest_app(config=base_config):
    """Returns an initialized Flask application."""
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)

    @app.route('/', methods=['GET'])
    def index():
        """Returns the applications index."""
        return "welcome to vsppm applications!"

    return app


def create_script_app(config=base_config):
    """Returns an initialized Flask application."""
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)

    manager = register_scripts(app)

    return manager


def register_extensions(app):
    """Register extensions with the Flask application."""
    db.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    rq.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    """Register blueprints with the Flask application."""
    app.register_blueprint(auth, url_prefix='/api/v1/auth')


def register_scripts(app):
    """Register script command with the Flask application."""
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    return manager
