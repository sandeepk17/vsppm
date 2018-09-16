#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Blueprint

auth = Blueprint('auth', __name__, static_folder='../../static', template_folder='../../templates')

from .views import index
from .views import user
from .views import company
from .views import department
from .views import group
from .views import role
from .views import acl
