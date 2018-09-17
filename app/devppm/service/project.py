#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app.devppm.models import VSProject
from app.database import DataTable
import json


class ProjectService:
    """
    项目服务
    """
    @classmethod
    def info(cls, id: int) -> (bool, dict, str):
        """
        根据id查询项目基本信息
        :param id: 项目id
        :return:
        """
        project = VSProject.query.filter_by(id=id).first_or_404()
        if project:
            data = project.to_dict()
            extra_data = ProjectService.__extra_info(data, project)
        else:
            return 50000, None, '项目基本信息不存在'

        return 20000, extra_data, '项目基本信息获取成功'

    @classmethod
    def list(cls, username, request) -> (bool, dict, str):
        """
        查询项目基本信息列表
        :param username: user'name of project member
        :param request: http request
        :return:
        """
        table = DataTable(
            model=VSProject,
            columns=[VSProject.id, VSProject.name, VSProject.type],
            sortable=[VSProject.id],
            searchable=[VSProject.name],
            filterable=[VSProject.type],
            limits=[25, 50, 100],
            request=request
        )

        data = []
        projects = table.items()
        for project in projects:
            project_dict = project.to_dict()
            extra_project_dict = ProjectService.__extra_info(project_dict, project)
            data.append(extra_project_dict)

        return 20000, data, '项目信息列表查询成功'

    @classmethod
    def update(cls, id, request) -> (bool, dict, str):
        """
        :param id : 项目id
        :param request: http request
        :return:
        """
        if request.is_json:
            args_data = request.get_json()
        else:
            args_data = json.loads(request.data)

        project = VSProject.query.filter_by(id=id).first_or_404()
        if project:
            new_project = project.update(**args_data)
            data = new_project.to_dict()
            extra_data = ProjectService.__extra_info(data, new_project)
        else:
            return 50000, {}, '项目基本信息更新失败'
        return 20000, extra_data, '项目信息更新成功'

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

        project = VSProject.create(**args_data)
        if project:
            data = project.to_dict()
            extra_data = ProjectService.__extra_info(data, project)
            return 20000, extra_data, '项目信息保存成功'

        return 50000, None, '项目信息保存失败'

    @classmethod
    def delete(cls, id: int) -> (bool, dict, str):
        """"
        :param id 项目id
        """
        project = VSProject.query.filter_by(id=id).first_or_404()
        if project:
            return 20000, project.delete(), '项目信息删除成功'

        return 50000, None, '项目基本信息删除失败'

    @classmethod
    def add_member(cls, project_id: int, member_id: int) -> (bool, dict, str):
        """
        :param project_id : 项目id
        :param member_id: 成员id
        :return:
        """
        return 20000, None, '项目成员添加成功'

    @classmethod
    def del_member(cls, project_id: int, member_id: int) -> (bool, dict, str):
        """
        :param project_id : 项目id
        :param member_id: 成员id
        :return:
        """
        return 20000, None, '项目成员删除成功'

    @classmethod
    def list_member(cls, project_id: int) -> (bool, dict, str):
        """
        :param project_id : 项目id
        :return:
        """
        return 20000, None, '获取项目成员列表成功'

    @classmethod
    def __extra_info(cls, data: dict, project):
        data['opened_by'] = {}
        if project.opened_by:
            data['opened_by'] = project.opened_by.to_dict()

        data['closed_by'] = {}
        if project.closed_by:
            data['closed_by'] = project.closed_by.to_dict()

        data['canceled_by'] = {}
        if project.canceled_by:
            data['canceled_by'] = project.canceled_by.to_dict()

        data['manager_admin'] = {}
        if project.manager_admin:
            data['manager_admin'] = project.manager_admin.to_dict()

        data['test_admin'] = {}
        if project.test_admin:
            data['test_admin'] = project.test_admin.to_dict()

        data['release_admin'] = {}
        if project.release_admin:
            data['release_admin'] = project.release_admin.to_dict()

        data['require_admin'] = {}
        if project.require_admin:
            data['require_admin'] = project.require_admin.to_dict()

        data['members'] = []
        if project.members:
            for member in project.members:
                data['members'].push(member.to_dict())

        data['company'] = {}
        if project.company:
            data['company'] = project.company.to_dict()

        data['department'] = {}
        if project.department:
            data['department'] = project.department.to_dict()

        return data
