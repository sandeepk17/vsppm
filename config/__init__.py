#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os


class base_config(object):
    """Default configuration options."""
    SITE_NAME = os.environ.get('APP_NAME', 'VSPPM')

    SERVER_HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    SERVER_PORT = os.environ.get('SERVER_PORT', '5000')

    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'mail')
    MAIL_PORT = os.environ.get('MAIL_PORT', 1025)

    REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
    REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
    RQ_REDIS_URL = 'redis://{}:{}'.format(REDIS_HOST, REDIS_PORT)

    MYSQL_HOST = os.environ.get('MYSQL_HOST', '47.104.184.107')
    MYSQL_PORT = os.environ.get('MYSQL_PORT', 3306)
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASS = os.environ.get('MYSQL_PASS', 'Red198594#')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'vsppm')

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (
        MYSQL_USER,
        MYSQL_PASS,
        MYSQL_HOST,
        MYSQL_PORT,
        MYSQL_DB
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SUPPORTED_LOCALES = ['en']

    JWT_SECRET = os.environ.get(
        'JWT_SECRET',
        'eyJsaWNlbnNlSWQiOiJLNzFVOERCUE5FIiwibGljZW5zZW')


class dev_config(base_config):
    """Development configuration options."""
    ASSETS_DEBUG = True

