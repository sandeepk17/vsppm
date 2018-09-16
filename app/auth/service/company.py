#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app.auth.models import VSCompany, VSDepartment, VSGroup
import json


class CompanyService:
    """
    公司服务
    """
    @classmethod
    def info(cls, id: int) -> (bool, dict, str):
        """
        :param id: 公司id
        :return:
        """
        company = VSCompany.query.filter_by(id=id).first_or_404()
        if company:
            return 20000, company.to_dict(), '公司基本信息查询成功'
        return 20000, None, '公司基本信息不存在'

    @classmethod
    def list(cls, request) -> (bool, dict, str):
        """
        :param request: http request
        :return:
        """
        data = []
        companys = VSCompany.query.all()
        for company in companys:
            data.append(company.to_dict())

        return 20000, data, '公司基本信息列表查询成功'

    @classmethod
    def update(cls, id: int, request) -> (bool, dict, str):
        """
        :param id : 公司id
        :param request: http request
        :return:
        """

        if request.is_json:
            args_data = request.get_json()
        else:
            args_data = json.loads(request.data)

        company = VSCompany.query.filter_by(id=id).first_or_404()
        if company:
            new_company = company.update(**args_data)
        else:
            return 50000, {}, '公司基本信息更新失败'

        return 20000, new_company.to_dict(), '公司基本信息更新成功'

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

        company = VSCompany.create(**args_data)
        if company:
            return 20000, company.to_dict(), '公司基本信息创建成功'

        return 50000, None, '公司基本信息创建失败'

    @classmethod
    def delete(cls, id: int) -> (bool, dict, str):
        """"
        :param id 公司id
        """
        company = VSCompany.query.filter_by(id=id).first_or_404()
        if company:
            # 循环删除部门信息
            departments = VSDepartment.query.filter_by(company_id=id).all()
            for department in departments:
                # 循环删除组信息
                groups = VSGroup.query.filter_by(departmrnt_id=department.id).all()
                for group in groups:
                    group.delete()

                department.delete()

            return 20000, company.delete(), '公司基本信息删除成功'

        return 50000, None, '公司基本信息删除失败'




