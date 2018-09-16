#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import (request, jsonify)
from lib.jwt import jwt_required
from app.auth import auth
from app.auth.service import DepartmentService


@auth.route('/department/info/<int:id>', methods=['GET'])
@jwt_required
def department_info(id):
    result, data, message = DepartmentService.info(id=id)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/department/list', methods=['GET'])
@jwt_required
def department_list():
    result, data, message = DepartmentService.list(request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/department/edit/<int:id>', methods=['PUT'])
@jwt_required
def department_edit(id):
    result, data, message = DepartmentService.update(id=id, request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/department/delete/<int:id>', methods=['DELETE'])
@jwt_required
def department_delete(id):
    result, data, message = DepartmentService.delete(id=id)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/department/create', methods=['POST'])
@jwt_required
def department_create():
    result, data, message = DepartmentService.create(request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }
