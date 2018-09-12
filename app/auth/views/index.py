#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app.auth import auth


@auth.route('/', methods=['GET'])
def index():
    return 'vsppm application auth module!'
