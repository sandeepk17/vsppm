#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app.devppm import devppm


@devppm.route('/', methods=['GET'])
def index():
    return 'vsppm application devppm module!'
