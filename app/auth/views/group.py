#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import (request, jsonify)
from lib.jwt import jwt_required
from app.auth import auth
from app.auth.service import GroupService


@auth.route('/group/info/<int:id>', methods=['GET'])
@jwt_required
def group_info(id):
    result, data, message = GroupService.info(id=id)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/group/list', methods=['GET'])
@jwt_required
def group_list():
    result, data, message = GroupService.list(request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/group/edit/<int:id>', methods=['PUT'])
@jwt_required
def group_edit(id):
    result, data, message = GroupService.update(id=id, request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/group/delete/<int:id>', methods=['DELETE'])
@jwt_required
def group_delete(id):
    result, data, message = GroupService.delete(id=id)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/group/create', methods=['POST'])
@jwt_required
def group_create():
    result, data, message = GroupService.create(request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }
