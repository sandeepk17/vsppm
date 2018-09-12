#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import (request, jsonify)
from lib.jwt import jwt_required
from app.auth import auth
from app.auth.service import RoleService


@auth.route('/role/info/<int:id>', methods=['GET'])
@jwt_required
def role_info(id):
    result, data, message = RoleService.info(id=id)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/role/list', methods=['GET'])
@jwt_required
def role_list():
    result, data, message = RoleService.list(request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/role/edit/<int:id>', methods=['PUT'])
@jwt_required
def use_edit(id):
    result, data, message = RoleService.update(id=id, request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/role/delete/<int:id>', methods=['DELETE'])
@jwt_required
def role_delete(id):
    result, data, message = RoleService.delete(id=id)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/role/create', methods=['POST'])
@jwt_required
def role_create():
    result, data, message = RoleService.create(request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }
