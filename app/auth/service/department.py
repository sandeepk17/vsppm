#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app.auth.models import VSDepartment
from lib.database import DataTable
import json


class DepartmentService:
    """
    部门服务
    """
    @classmethod
    def info(cls, id: int) -> (bool, dict, str):
        """
        :param id: 部门id
        :return:
        """
        return 20000, VSDepartment.query.filter_by(id=id).first_or_404(), '部门基本信息查询成功'

    @classmethod
    def list(cls, request) -> (bool, dict, str):
        """
        :param request: http request
        :return:
        """
        datatable = DataTable(
            model=VSDepartment,
            columns=[VSDepartment.id, VSDepartment.name, VSDepartment.grade, VSDepartment.admin],
            sortable=[],
            searchable=[VSDepartment.name],
            filterable=[VSDepartment.active],
            limits=[25, 50, 100],
            request=request
        )

        return 20000, datatable.query.items(), '部门基本信息列表查询成功'

    @classmethod
    def update(cls, id: int, request) -> (bool, dict, str):
        """
        :param id : 部门id
        :param request: http request
        :return:
        """

        if request.is_json:
            args_data = request.get_json()
        else:
            args_data = json.loads(request.data)

        department = VSDepartment.query.filter_by(id=id).first_or_404()
        return 20000, department.update(**args_data), '部门基本信息更新成功'

    @classmethod
    def create(cls, request) -> (bool, dict, str):
        """
        :param request: http request
        :return:
        """

        if request.is_json:
            args_data = request.get_json()
        else:
            args_data = json.loads(request.data)

        return 20000, VSDepartment.create(**args_data), '部门基本信息创建成功'

    @classmethod
    def delete(cls, id: int) -> (bool, dict, str):
        """"
        :param id 部门id
        """
        department = VSDepartment.query.filter_by(id=id).first_or_404()
        return 20000, department.delete(), '部门基本信息删除成功'


