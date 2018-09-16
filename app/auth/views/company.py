#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import (request, jsonify)
from lib.jwt import jwt_required
from app.auth import auth
from app.auth.service import CompanyService


@auth.route('/company/info/<int:id>', methods=['GET'])
@jwt_required
def company_info(id):
    result, data, message = CompanyService.info(id=id)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/company/list', methods=['GET'])
@jwt_required
def company_list():
    result, data, message = CompanyService.list(request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/company/edit/<int:id>', methods=['PUT'])
@jwt_required
def company_edit(id):
    result, data, message = CompanyService.update(id=id, request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/company/delete/<int:id>', methods=['DELETE'])
@jwt_required
def company_delete(id):
    result, data, message = CompanyService.delete(id=id)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/company/create', methods=['POST'])
@jwt_required
def company_create():
    result, data, message = CompanyService.create(request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }
