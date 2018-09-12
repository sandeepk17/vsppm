#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_migrate import Migrate
from flask_rq2 import RQ

bcrypt = Bcrypt()
mail = Mail()
migrate = Migrate()
rq = RQ()
