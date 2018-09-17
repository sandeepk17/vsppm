#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
from app.database import db, CRUDMixin

vsppm_project_member = db.Table(
    'tbl_vsppm_project_member',
    db.Column(
        'user_id',
        db.Integer,
        db.ForeignKey('tbl_vsppm_user.id'),
        primary_key=True),
    db.Column(
        'project_id',
        db.Integer,
        db.ForeignKey('tbl_vsppm_project.id'),
        primary_key=True))


class VSProject(CRUDMixin, db.Model):
    """"
    项目模型
    """
    __tablename__ = 'tbl_vsppm_project'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 名称
    name = db.Column(db.String(90), nullable=False, unique=True)
    # 开始日期
    begin = db.Column(db.Date())
    # 结束日期
    end = db.Column(db.Date())
    # 项目类型
    type = db.Column(db.String(20), default='sprint')
    # 历时天数
    days = db.Column(db.Integer)
    # 状态
    status = db.Column(db.String(30), default='wait')
    # 描述
    desc = db.Column(db.String(256))
    # 公司id
    company_id = db.Column(db.Integer,
                              db.ForeignKey('tbl_vsppm_company.id'))
    # 部门id
    department_id = db.Column(db.Integer,
                              db.ForeignKey('tbl_vsppm_department.id'))
    # 项目开启者
    opened_by_id = db.Column(db.Integer,
                             db.ForeignKey('tbl_vsppm_user.id'))
    # 项目开启日期
    opened_datetime = db.Column(db.DateTime(timezone=True))
    # 项目关闭者
    closed_by_id = db.Column(db.Integer,
                             db.ForeignKey('tbl_vsppm_user.id'))
    # 项目关闭日期
    closed_datetime = db.Column(db.DateTime(timezone=True))
    # 项目取消者
    canceled_by_id = db.Column(db.Integer,
                               db.ForeignKey('tbl_vsppm_user.id'))
    # 项目取消日期
    canceled_datetime = db.Column(db.DateTime(timezone=True))
    # 项目管理员id
    manager_admin_id = db.Column(db.Integer,
                                 db.ForeignKey('tbl_vsppm_user.id'))
    # 测试管理员id
    test_admin_id = db.Column(db.Integer,
                              db.ForeignKey('tbl_vsppm_user.id'))
    # 发布管理员id
    release_admin_id = db.Column(db.Integer,
                                 db.ForeignKey('tbl_vsppm_user.id'))
    # 需求管理员id
    require_admin_id = db.Column(db.Integer,
                                 db.ForeignKey('tbl_vsppm_user.id'))
    access = db.Column(db.String(20), default='open')
    # 创建时间
    created_ts = db.Column(
        db.DateTime(timezone=True),
        default=datetime.datetime.utcnow
    )
    # 更新时间
    updated_ts = db.Column(
        db.DateTime(timezone=True),
        default=datetime.datetime.utcnow
    )
    # 激活状态
    active = db.Column(db.Boolean(), default=True)

    # http://docs.sqlalchemy.org/en/rel_0_9/orm/join_conditions.html#handling-multiple-join-paths
    opened_by = db.relationship('VSUser', foreign_keys=[opened_by_id])
    closed_by = db.relationship('VSUser', foreign_keys=[closed_by_id])
    canceled_by = db.relationship('VSUser', foreign_keys=[canceled_by_id])
    manager_admin = db.relationship('VSUser', foreign_keys=[manager_admin_id])
    test_admin = db.relationship('VSUser', foreign_keys=[test_admin_id])
    release_admin = db.relationship('VSUser', foreign_keys=[release_admin_id])
    require_admin = db.relationship('VSUser', foreign_keys=[require_admin_id])

    # 项目成员
    members = db.relationship('VSUser', secondary=vsppm_project_member, backref=db.backref('projects'))
    company = db.relationship('VSCompany', backref=db.backref('projects'))
    department = db.relationship('VSDepartment', backref=db.backref('projects'))

    def __init__(self, **kwargs):
        super(VSProject, self).__init__(**kwargs)

    def __repr__(self):
        return '<VSProject #%s:%r>' % (self.id, self.name)
