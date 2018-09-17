#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app.devppm.models import VSProject


class DashboardService:
    """
    项目统计分析服务
    """
    @classmethod
    def list_projects_filter_by_status(cls, request) -> (bool, dict, str):
        status = request.values.get('status', None)
        data = []
        if status:
            projects = VSProject.query.filter_by(status=status).all()
            for project in projects:
                data.append(project.to_dict())

        return 20000, data, '项目信息列表依据状态分类查询成功'

    @classmethod
    def count_projects(cls) -> (bool, dict, str):
        # 总数
        all_count = VSProject.query.count()
        # 未开始数量
        wait_count = VSProject.query.filter_by(status='wait').count()
        # 进行中数量
        doing_count = VSProject.query.filter_by(status='doing').count()
        # 挂起数量
        suspended_count = VSProject.query.filter_by(status='suspended').count()
        # 关闭数量
        closed_count = VSProject.query.filter_by(status='closed').count()

        data = {
            'all': all_count,
            'wait': wait_count,
            'doing': doing_count,
            'suspended': suspended_count,
            'closed': closed_count
        }

        return 20000, data, '项目总数查询成功'

