#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Blueprint

devppm = Blueprint('devppm', __name__, static_folder='../../static', template_folder='../../templates')

from .views import index
from .views import project
from .views import member
from .views import dashboard
