# -*- coding: utf-8 -*-


from flask import request
from apps.user_api_v1 import user_api_v1 as user_bp
from apps.user_api_v1.model import User
from apps import db


@user_bp.route('/register', methods=["POST"])
def register_user():
    """
    create user
    :return:
    """

    error_msg = {
        "data": None,
        "response": "failed",
        "msg": ""
    }

    request_body = request.json
    if not request_body:
        error_msg["msg"] = "Lack of body"
        return error_msg, 200

    username = request_body.get("username", None)
    password = request_body.get("password", None)
    password2 = request_body.get("password2", None)
    phone = request_body.get("phone", None)

    # verify params
    if not all([username, password, password2, phone]):
        error_msg["msg"] = "Lack of parameter"
        return error_msg, 200

    if password != password2:
        error_msg["msg"] = "password2 != password"
        return error_msg, 200

    try:
        user_list = User.query.filter_by(phoneNumber=phone).all()
        print(f"user_list: {user_list}")
    except Exception as e:
        print("find user failed")
        print(e)
        error_msg["msg"] = "Database exception"
        return error_msg, 200

    if user_list:
        error_msg["msg"] = "The phone has been registered"
        return error_msg, 200

    user = User(userName=username, phoneNumber=phone, passWord=password)
    print(f"New user info: {user}")

    try:
        db.session.add(user)
        db.session.commit()
        return {
            "data": {
                "uid": user.id
            },
            "response": "successful",
            "msg": "0"
        }, 201
    except Exception as e:
        print(e)
        error_msg["msg"] = "Add user fail"
        return error_msg, 200


@user_bp.route('/login', methods=["POST"])
def login():
    """
    user login
    :return:
    """

    error_msg = {
        "data": None,
        "response": "failed",
        "msg": ""
    }

    # get username and pwd from body
    request_body = request.json
    if not request_body:
        error_msg["msg"] = "Lack of body"
        return error_msg, 200

    # verify params
    username = request_body.get("username", None)
    password = request_body.get("password", None)

    if not all([username, password]):
        error_msg["msg"] = "Lack of parameter"
        return error_msg, 200

    try:
        user_list = User.query.filter_by(userName=username).all()
        print(f"user {user_list} login")
    except Exception as e:
        print(e)
        error_msg["msg"] = "Database exception"
        return error_msg, 200

    if not user_list:
        error_msg["msg"] = "Database exception"
        return error_msg, 200

    user = user_list[0]

    # verify password
    if password != user.passWord:
        error_msg["msg"] = "Password is wrong, please try again"
        return error_msg, 200

    return {
        "data": {
            "user": user.userName
        },
        "response": "success",
        "msg": "0"
    }