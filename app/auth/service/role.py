#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app.auth.models import VSRole
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
        role = VSRole.query.filter_by(id=id).first_or_404()
        if role:
            return 20000, role.to_dict(), '角色基本信息查询成功'
        return 20000, None, '角色基本信息不存在'

    @classmethod
    def list(cls, request) -> (bool, dict, str):
        """
        :param request: http request
        :return:
        """
        data = []
        roles = VSRole.query.all()
        for role in roles:
            data.append(role.to_dict())

        return 20000, data, '角色基本信息列表查询成功'

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
        if role:
            new_role = role.update(**args_data)
        else:
            return 50000, {}, '角色基本信息更新失败'

        return 20000, new_role.to_dict(), '角色基本信息更新成功'

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

        role = VSRole.create(**args_data)
        if role:
            return 20000, role.to_dict(), '角色基本信息创建成功'

        return 50000, None, '角色基本信息创建失败'

    @classmethod
    def delete(cls, id: int) -> (bool, dict, str):
        """"
        :param id 角色id
        """
        role = VSRole.query.filter_by(id=id).first_or_404()
        if role:
            return 20000, role.delete(), '角色基本信息删除成功'

        return 50000, None, '角色基本信息删除失败'

