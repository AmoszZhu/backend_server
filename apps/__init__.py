# -*- coding: utf-8 -*-

"""
init app
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from werkzeug.utils import import_string
import os

db = SQLAlchemy()

def create_app():
    """
    create app with config file
    :return: app
    """
    app = Flask(__name__)
    config_name = os.environ.get('APP_CONFIG', 'config.TestConfig')
    print(f"This project is using {config_name} env now")

    # use config file
    app.config.from_object(config_name)

    #init db
    db.init_app(app)

    CORS(app)

    # register blueprint
    register_blueprint(app)

    return app


def register_blueprint(app):
    apps_absolute_path = os.path.dirname(__file__)
    base_file = apps_absolute_path.split("/")[-1]
    file_list = os.listdir(apps_absolute_path)
    for file_name in file_list:
        file_path = os.path.join(apps_absolute_path, file_name)
        if not os.path.isdir(file_path):
            continue
        if not os.path.exists(os.path.join(apps_absolute_path, "__init__.py")):
            continue
        if file_name == "__pycache__":
            continue
        blueprint_name = base_file + '.' + file_name + ":" + file_name
        print(f"bp name is {blueprint_name}")
        auto_blueprint = import_string(blueprint_name)
        app.register_blueprint(auto_blueprint)


# create app
app = create_app()

# 使用数据库迁移
migrate = Migrate(app, db)





