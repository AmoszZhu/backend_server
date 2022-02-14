# -*- coding: utf-8 -*-

from tools.jwt_util import generate_jwt
from datetime import datetime, timedelta
from flask import current_app


def generate_token(user_id, refresh=True):
    """

    :param user_id:
    :param refresh:
    :return:
    """
    jwt_timeout = current_app.config["JWT_TIMEOUT"]
    if not jwt_timeout:
        jwt_timeout = 2
    expire = datetime.utcnow() + timedelta(hours=jwt_timeout)

    token = generate_jwt({
        "user_id": user_id,
    }, expire=expire)

    if refresh:
        expire = datetime.utcnow() + timedelta(days=14)
        refresh_token = generate_jwt({
            "user_id": user_id,
            "is_refresh": True
        }, expire=expire)
    else:
        refresh_token = None

    return token, refresh_token
