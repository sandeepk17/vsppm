#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app.auth.models import VSAcl
from lib.database import DataTable
import json


class AclService:
    """
    权限服务
    """

    @classmethod
    def info(cls, id: int) -> (bool, dict, str):
        """
        :param id: 权限id
        :return:
        """
        return 20000, VSAcl.query.filter_by(id=id).first_or_404(), '权限基本信息查询成功'

    @classmethod
    def list(cls, request) -> (bool, dict, str):
        """
        :param request: http request
        :return:
        """
        datatable = DataTable(
            model=VSAcl,
            columns=[VSAcl.id, VSAcl.module, VSAcl.method],
            sortable=[],
            searchable=[],
            filterable=[VSAcl.active],
            limits=[25, 50, 100],
            request=request
        )

        return 20000, datatable.query.items(), '权限基本信息列表查询成功'

    @classmethod
    def update(cls, id: int, request) -> (bool, dict, str):
        """
        :param id 权限id
        :param request: http request
        :return:
        """

        if request.is_json:
            args_data = request.get_json()
        else:
            args_data = json.loads(request.data)

        acl = VSAcl.query.filter_by(id=id).first_or_404()
        return 20000, acl.update(**args_data), '权限基本信息更新成功'

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

        return 20000, VSAcl.create(**args_data), '权限创建成功'

    @classmethod
    def delete(cls, id: int) -> (bool, dict, str):
        """"
        :param id 权限id
        :return
        """
        acl = VSAcl.query.filter_by(id=id).first_or_404()
        return 20000, acl.delete(), '权限删除成功'
