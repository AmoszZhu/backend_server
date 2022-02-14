# -*- coding: utf-8 -*-

from apps import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(120), unique=True)
    phoneNumber = db.Column(db.String(120), unique=True)
    passWord = db.Column(db.String(120), unique=False)

    def __repr__(self):
        return '<User : %s>' % self.userName