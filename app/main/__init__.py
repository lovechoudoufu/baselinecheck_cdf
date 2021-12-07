#!/usr/bin/python3
# -*- coding:utf-8 -*-

from flask import Blueprint

main = Blueprint('main', __name__)

from . import errors, view
