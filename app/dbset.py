#!/usr/bin/python3
# -*- coding:utf-8 -*-


import json

from flask_login import UserMixin
from peewee import Model, CharField, IntegerField, SqliteDatabase
from werkzeug.security import check_password_hash, generate_password_hash
from app import login_manager
from conf.config import config

cfg = config['default']

db = SqliteDatabase(cfg.DB_FILE, timeout=10, check_same_thread=False)


class BaseModel(Model):
    class Meta:
        database = db

    def __str__(self):
        r = {}
        for k in self._data.keys():
            try:
                r[k] = str(getattr(self, k))
            except:
                r[k] = json.dumps(getattr(self, k))

        return json.dumps(r, ensure_ascii=False)


class User(UserMixin, BaseModel):
    __tablename__ = 'user'
    id = IntegerField()
    username = CharField()
    password = CharField()
    email = CharField()

    def verify_password(self, raw_password):
        return check_password_hash(self.password, raw_password)

    def update_password(self, username, raw_password):
        new_password_hash = generate_password_hash(raw_password)
        User.update(password=new_password_hash).where(User.username == username).execute()


class Tasklist(UserMixin, BaseModel):
    __tablename__ = 'tasklist'
    theorder = CharField()
    time = CharField()
    status = CharField()
    note = CharField()


@login_manager.user_loader
def load_user(user_id):
    return User.get(User.id == int(user_id))
