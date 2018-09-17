#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import request
from app.devppm import devppm
from app.devppm.service import DashboardService
from lib.jwt import jwt_required


@devppm.route('/project/dashboard/count', methods=['GET'])
@jwt_required
def project_dash_count():
    result, data, message = DashboardService.count_projects()
    return {
        'result': result,
        'data': data,
        'message': message
    }


@devppm.route('/project/dashboard/status_filter', methods=['GET'])
@jwt_required
def project_dash_status_filter():
    result, data, message = DashboardService.list_projects_filter_by_status(request=request)
    return {
        'result': result,
        'data': data,
        'message': message
    }