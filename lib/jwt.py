#!/usr/bin/python3
# -*- coding: utf-8 -*-

import jwt
from functools import wraps
from flask import (request, jsonify)

from config import base_config
from .log import logger


class JwtDecoder(object):
    def __init__(self, token="", secret=base_config.JWT_SECRET):
        self.secret = secret
        self.token = token

    def get_value(self, token: str, key: str) -> (bool, str):
        """"
            :param token jwt auth token
            :param key main key in token
            :return
            bool: function exec result
            str: function exec data
        """
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return True, payload[key]
        except Exception as e:
            logger.debug("异常: {}".format(e))
            return False, ''

    def get(self, key: str) -> (bool, str):
        """"
            :param key main key in token
            :return
            bool: function exec result
            str: function exec data
        """
        try:
            payload = jwt.decode(self.token, self.secret, algorithms=['HS256'])
            return True, payload[key]
        except Exception as e:
            logger.debug("异常: {}".format(e))
            return False, ''


class JwtEncoder(object):
    def __init__(self, secret=base_config.JWT_SECRET):
        self.secret = secret

    def encoder(self, payload: dict) ->(bool, str):
        """"
            :param payload  format as {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=36000),
                'iat': datetime.datetime.utcnow(),
                'iss': 'ken',
                'data': {
                    'username': username
                }
            }
            :return
            bool: function exec result
            str: function exec data
        """

        try:
            token = jwt.encode(
                payload,
                self.secret,
                algorithm='HS256'
            )
            return True, token
        except Exception as e:
            return False, "异常: {}".format(e)


def jwt_required_response_form(result, data='', message=''):
    return {
        'result': result,
        'data': data,
        'message': message
    }


def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(request.headers)
        token = request.headers.get('X-Token')
        if token:
            r, data = JwtDecoder(token).get('data')
            if r:
                return jsonify(fn(*args, **kwargs))
            else:
                return jsonify(jwt_required_response_form(
                    result=50000,
                    data='',
                    message='认证无效'))
        else:
            return jsonify(jwt_required_response_form(
                result=50000,
                data='',
                message='没有提供认证token'))

    return wrapper


def jwt_required_payload(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(request.headers)
        token = request.headers.get('X-Token')
        if token:
            r, data = JwtDecoder(token).get('data')
            if r:
                kwargs.setdefault("username", data['username'])
                return jsonify(fn(*args, **kwargs))
            else:
                return jsonify(jwt_required_response_form(
                    result=50000,
                    data='',
                    message='认证无效'))
        else:
            return jsonify(jwt_required_response_form(
                result=50000,
                data='',
                message='没有提供认证token'))

    return wrapper