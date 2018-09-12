#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app import create_script_app
from config import dev_config

app = create_script_app(dev_config)

app.run()
