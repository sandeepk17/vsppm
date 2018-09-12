#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import (request, jsonify)
from lib.jwt import jwt_required
from app.auth import auth
from app.auth.service import AclService


@auth.route('/acl/info/<int:id>', methods=['GET'])
@jwt_required
def acl_info(id):
    result, data, message = AclService.info(id=id)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/acl/list', methods=['GET'])
@jwt_required
def acl_list():
    result, data, message = AclService.list(request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/acl/edit/<int:id>', methods=['PUT'])
@jwt_required
def use_edit(id):
    result, data, message = AclService.update(id=id, request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/acl/delete/<int:id>', methods=['DELETE'])
@jwt_required
def acl_delete(id):
    result, data, message = AclService.delete(id=id)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/acl/create', methods=['POST'])
@jwt_required
def acl_create():
    result, data, message = AclService.create(request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }
