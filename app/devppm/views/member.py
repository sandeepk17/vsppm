#!/usr/bin/python3
# -*- coding: utf-8 -*-

from lib.jwt import jwt_required
from app.devppm import devppm
from app.devppm.service import ProjectService


@devppm.route('/project/<int:project_id>/member/<int:member_id>', methods=['POST'])
@jwt_required
def add_member(project_id, member_id):
    result, data, message = ProjectService.add_member(project_id=project_id, member_id=member_id)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@devppm.route('/project/<int:project_id>/member/<int:member_id>', methods=['DELETE'])
@jwt_required
def del_member(project_id, member_id):
    result, data, message = ProjectService.del_member(project_id=project_id, member_id=member_id)
    return {
        'result': result,
        'data': data,
        'message': message
    }


@devppm.route('/project/<int:project_id>/member/list', methods=['GET'])
@jwt_required
def list_member(project_id):
    result, data, message = ProjectService.list_member(project_id=project_id)
    return {
        'result': result,
        'data': data,
        'message': message
    }