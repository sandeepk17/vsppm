#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app import create_rest_app
from config import dev_config


app = create_rest_app(dev_config)

app.run(host=dev_config.SERVER_HOST, port=dev_config.SERVER_PORT, debug=dev_config.ASSETS_DEBUG)
