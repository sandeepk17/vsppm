#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import request
from lib.jwt import jwt_required, jwt_required_payload
from app.devppm import devppm
from app.devppm.service import ProjectService


@devppm.route('/project/info/<int:id>', methods=['GET'])
@jwt_required
def project_info(id):
    result, data, message = ProjectService.info(id=id)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@devppm.route('/project/list', methods=['GET'])
@jwt_required_payload
def project_list(username):
    result, data, message = ProjectService.list(username=username, request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@devppm.route('/project/edit/<int:id>', methods=['PUT'])
@jwt_required
def project_edit(id):
    result, data, message = ProjectService.update(id=id, request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@devppm.route('/project/delete/<int:id>', methods=['DELETE'])
@jwt_required
def project_delete(id):
    result, data, message = ProjectService.delete(id=id)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@devppm.route('/project/create', methods=['POST'])
@jwt_required
def project_create():
    result, data, message = ProjectService.create(request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }
