#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Blueprint

auth = Blueprint('auth', __name__, static_folder='../../static', template_folder='../../templates')

from . import views
