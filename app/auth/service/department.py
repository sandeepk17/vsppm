#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app.auth.models import VSDepartment, VSCompany, VSGroup
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
        department = VSDepartment.query.filter_by(id=id).first_or_404()
        if department:
            return 20000, department.to_dict(), '部门基本信息查询成功'
        return 20000, None, '部门基本信息不存在'

    @classmethod
    def list(cls, request) -> (bool, dict, str):
        """
        :param request: http request
        :return:
        """
        # 部门表记录集合
        data = []

        # 查询公司是否存在
        company_id = request.args.get("company_id", default=0)
        company = VSCompany.query.filter_by(id=company_id).first_or_404()
        if company:
            # 获取部门
            departments = VSDepartment.query.filter_by(company_id=company_id).all()
            for department in departments:
                data.append(department.to_dict())

        return 20000, data, '部门基本信息列表查询成功'

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
        if department:
            new_department = department.update(**args_data)
        else:
            return 50000, {}, '部门基本信息更新失败'

        return 20000, new_department.to_dict(), '部门基本信息更新成功'

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

        department = VSDepartment.create(**args_data)
        if department:
            return 20000, department.to_dict(), '部门基本信息创建成功'

        return 50000, None, '部门基本信息创建失败'

    @classmethod
    def delete(cls, id: int) -> (bool, dict, str):
        """"
        :param id 部门id
        """
        department = VSDepartment.query.filter_by(id=id).first_or_404()
        if department:
            # 循环删除组信息
            groups = VSGroup.query.filter_by(departmrnt_id=department.id).all()
            for group in groups:
                group.delete()

            return 20000, department.delete(), '部门基本信息删除成功'

        return 50000, None, '部门基本信息删除失败'


