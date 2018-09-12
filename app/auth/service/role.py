#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app.auth.models import VSRole
from lib.database import DataTable
import json


class RoleService:
    """
    角色服务
    """
    @classmethod
    def info(cls, id: int) -> (bool, dict, str):
        """
        :param id: 角色id
        :return:
        """
        return 20000, VSRole.query.filter_by(id=id).first_or_404(), '角色基本信息查询成功'

    @classmethod
    def list(cls, request) -> (bool, dict, str):
        """
        :param request: http request
        :return:
        """
        datatable = DataTable(
            model=VSRole,
            columns=[VSRole.id, VSRole.name],
            sortable=[],
            searchable=[],
            filterable=[VSRole.active],
            limits=[25, 50, 100],
            request=request
        )

        return 20000, datatable.query.items(), '角色信息列表查询成功'

    @classmethod
    def update(cls, id: int, request) -> (bool, dict, str):
        """
        :param request: http request
        :return:
        """
        if request.is_json:
            args_data = request.get_json()
        else:
            args_data = json.loads(request.data)

        role = VSRole.query.filter_by(id=id).first_or_404()
        role.update(**args_data)

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

        return 20000, VSRole.create(**args_data), '角色创建成功'

    @classmethod
    def delete(cls, id: int) -> (bool, dict, str):
        """"
        :param id 角色id
        """
        role = VSRole.query.filter_by(id=id).first_or_404()
        return 20000, role.delete(), '角色基本信息删除成功'

