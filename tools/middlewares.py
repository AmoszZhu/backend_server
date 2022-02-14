# -*- coding: utf-8 -*-

from flask import request, g
from tools.jwt_util import verify_jwt


def verify_token():
    g.user_id = None
    g.is_refresh = None

    token = request.headers.get("Authorization")
    print(f"token is {token}")
    if token is not None and token.startswith("Bearer "):
        token = token[7:]

        payload = verify_jwt(token)

        if payload is not None:
            g.user_id = payload.get("user_id")
            g.is_refresh = payload.get("is_refresh", False)
            print(g.is_refresh, g.user_id)
