# -*- coding: utf-8 -*-

"""
init app
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
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

    return app


# create app
app = create_app()

# 使用数据库迁移
migrate = Migrate(app, db)





