# -*- coding: utf-8 -*-

"""
1. jwt组成
    header,payload,signature
    a. header 头部
"""

from flask import current_app
import jwt


def generate_jwt(payload, expire, sercet=None):
    """

    :param payload: dict 载荷
    :param expire: datetime 过期时间
    :param sercet: 密钥
    :return:
    """
    _payload = {
        'exp': expire
    }
    _payload.update(payload)

    if not sercet:
        sercet = current_app.config['JWT_SECRET']

    token = jwt.encode(payload=_payload, key=sercet, algorithm='HS256')
    return token


def verify_token(token, sercet=None):
    """

    :param token:
    :param sercet:
    :return:
    """
    if not sercet:
        sercet = current_app.config['JWT_SECRET']

    try:
        _payload = jwt.decode(token, sercet, algorithm='HS256')
    except jwt.PyJWTError:
        _payload = None

    return _payload
