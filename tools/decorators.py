# -*- coding: utf-8 -*-

"""
定义装饰器
"""

from flask import g
from functools import wraps


def login_requeried(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if g.user_id is not None and g.is_refresh is False:
            return func(*args, **kwargs)
        else:
            return {
                "data": None,
                "response": "failed",
                "msg": "Invalied user"
            }

    return wrapper
