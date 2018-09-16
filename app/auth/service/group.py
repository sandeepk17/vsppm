#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app.auth.models import VSDepartment, VSGroup
import json


class GroupService:
    """
    组服务
    """
    @classmethod
    def info(cls, id: int) -> (bool, dict, str):
        """
        :param id: 组id
        :return:
        """
        group = VSGroup.query.filter_by(id=id).first_or_404()
        if group:
            return 20000, group.to_dict(), '组基本信息查询成功'
        return 20000, None, '组基本信息不存在'

    @classmethod
    def list(cls, request) -> (bool, dict, str):
        """
        :param request: http request
        :return:
        """
        # 组表记录集合
        data = []

        # 查询部门是否存在
        department_id = request.args.get("department_id", default=0)
        department = VSDepartment.query.filter_by(id=department_id).first_or_404()
        if department:
            # 获取组
            groups = VSGroup.query.filter_by(department_id=department_id).all()
            for group in groups:
                data.append(group.to_dict())

        return 20000, data, '组基本信息列表查询成功'

    @classmethod
    def update(cls, id: int, request) -> (bool, dict, str):
        """
        :param id : 组id
        :param request: http request
        :return:
        """

        if request.is_json:
            args_data = request.get_json()
        else:
            args_data = json.loads(request.data)

        group = VSGroup.query.filter_by(id=id).first_or_404()
        if group:
            new_group = group.update(**args_data)
        else:
            return 50000, {}, '组基本信息更新失败'

        return 20000, new_group.to_dict(), '组基本信息更新成功'

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

        group = VSGroup.create(**args_data)
        if group:
            return 20000, group.to_dict(), '组基本信息创建成功'

        return 50000, None, '组基本信息创建失败'

    @classmethod
    def delete(cls, id: int) -> (bool, dict, str):
        """"
        :param id 组id
        """
        group = VSGroup.query.filter_by(id=id).first_or_404()
        if group:
            return 20000, group.delete(), '组基本信息删除成功'

        return 50000, None, '组基本信息删除失败'


