#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app.auth.models import VSUser, VSRole, VSDepartment
from lib.database import DataTable
import json


class UserService:
    """
    账户服务
    """
    @classmethod
    def info(cls, username: str) -> (bool, dict, str):
        """
        根据username查询账户基本信息
        :param username: 账户名称
        :return:
        """
        user = VSUser.query.filter_by(username=username).first_or_404()
        if user:
            data = user.to_dict()

            # 查询部门所属信息
            if user.department_id:
                department = VSDepartment.query.filter_by(id=user.department_id).first_or_404()
                if department:
                    data['department'] = department.to_dict()
                else:
                    data['department'] = {}
            else:
                data['department'] = {}

            # 查询所属角色信息
            if user.role_id:
                role = VSRole.query.filter_by(id=user.role_id).first_or_404()
                if role:
                    data['role'] = role.to_dict()
                else:
                    data['role'] = {}
            else:
                data['role'] = {}
        else:
            return 50000, None, '账户基本信息不存在'

        return 20000, data, '账户基本信息获取成功'

    @classmethod
    def list(cls, request) -> (bool, dict, str):
        """
        查询账户基本信息列表
        :param request: http request
        :return:
        """
        datatable = DataTable(
            model=VSUser,
            columns=[VSUser.id, VSUser.username, VSUser.email],
            sortable=[],
            searchable=[VSUser.username],
            filterable=[VSUser.active],
            limits=[25, 50, 100],
            request=request
        )

        return 20000, datatable.query.items(), '账户信息列表查询成功'

    @classmethod
    def update(cls, id, request) -> (bool, dict, str):
        """
        :param id : 账户id
        :param request: http request
        :return:
        """
        if request.is_json:
            args_data = request.get_json()
        else:
            args_data = json.loads(request.data)

        user = VSUser.query.filter_by(id=id).first_or_404()
        return 20000, user.update(**args_data), '账户信息更新成功'

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

        return 20000, VSUser.create(**args_data), '账户信息保存成功'

    @classmethod
    def delete(cls, id: int) -> (bool, dict, str):
        """"
        :param id 账户id
        """
        user = VSUser.query.filter_by(id=id).first_or_404()
        return 20000, user.delete(), '账户信息删除成功'

    @classmethod
    def login(cls, request) -> (bool, dict, str):
        """
        登陆验证
        :param request:
        :return:
        """
        if request.is_json:
            args_data = request.get_json()
        else:
            args_data = json.loads(request.data)

        # 查询账户基本信息
        user = VSUser.query.filter_by(
            username=args_data['username']).first_or_404()
        if user:
            # 验证密码
            final = user.check_password(args_data['password'])
            if final:
                r, token = user.generate_token()
                if r:
                    result = 20000
                    data = {'token': token}
                    message = '登陆成功!'
                else:
                    result = 50000
                    data = {}
                    message = '授权失败!'
            else:
                result = 50000
                data = {}
                message = '密码校验失败!'
        else:
            result = 50000
            data = {}
            message = '帐户名不存在!'

        return result, data, message

    @classmethod
    def logout(cls, username: str) -> (bool, dict, str):
        """
        退出登录
        :param username: 账户名称
        :return:
        """
        return 20000, username, '退出登录成功'

    @classmethod
    def register(cls, request) -> (bool, dict, str):
        if request.is_json:
            args_data = request.get_json()
        else:
            args_data = json.loads(request.data)

        return 20000, VSUser.create(**args_data), '注册成功'

    @classmethod
    def update_role(cls, request) -> (bool, dict, str):
        if request.is_json:
            args_data = request.get_json()
        else:
            args_data = json.loads(request.data)

        return 20000, VSUser.create(**args_data), '更新角色成功'
