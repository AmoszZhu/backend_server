# -*- coding: utf-8 -*-

"""
config file
"""


# base config
class BaseConfig:
    SECRET_KEY = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'


# dev config
class DevConfig(BaseConfig):
    DEBUG = False


# test config
class TestConfig(BaseConfig):
    DEBUG = True

    # mysql
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:zj122900@beacon01.com:3306/server?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # jwt
    JWT_SECRET = "beacon_project"

    JWT_TIMEOUT = 2
