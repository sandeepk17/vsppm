#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import (request, jsonify)
from lib.jwt import jwt_required, jwt_required_payload
from app.auth import auth
from app.auth.service import UserService


@auth.route('/user/login', methods=['POST'])
def login():
    result, data, message = UserService.login(request=request)
    return jsonify({
        'result': result,
        'data': data,
        'message': message
    })


@auth.route('/user/logout', methods=['GET'])
@jwt_required
def logout():
    result, data, message = UserService.logout(username='')
    return jsonify({
        'result': result,
        'data': data,
        'message': message
    })


@auth.route('/user/register', methods=['POST'])
def register():
    result, data, message = UserService.register(request=request)
    return jsonify({
        'result': result,
        'data': data,
        'message': message
    })


@auth.route('/user/info', methods=['GET'])
@jwt_required_payload
def user_info(username):
    result, data, message = UserService.info(username=username)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/user/list', methods=['GET'])
@jwt_required
def user_list():
    result, data, message = UserService.list(request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/user/edit/<int:id>', methods=['PUT'])
@jwt_required
def use_edit(id):
    result, data, message = UserService.update(id=id, request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/user/delete/<int:id>', methods=['DELETE'])
@jwt_required
def user_delete(id):
    result, data, message = UserService.delete(id=id)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/user/create', methods=['POST'])
@jwt_required
def user_create():
    result, data, message = UserService.create(request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@auth.route('/user/role', methods=['PUT'])
@jwt_required
def user_role():
    result, data, message = UserService.update_role(request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }