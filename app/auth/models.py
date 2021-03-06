#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime

from app.database import db, CRUDMixin
from lib.extensions import bcrypt
from lib.jwt import JwtEncoder

vsppm_group_user = db.Table(
    'tbl_vsppm_group_user',
    db.Column(
        'group_id',
        db.Integer,
        db.ForeignKey('tbl_vsppm_group.id'),
        primary_key=True),
    db.Column(
        'user_id',
        db.Integer,
        db.ForeignKey('tbl_vsppm_user.id'),
        primary_key=True))

vsppm_role_acl = db.Table(
    'tbl_vsppm_role_acl',
    db.Column(
        'role_id',
        db.Integer,
        db.ForeignKey('tbl_vsppm_role.id'),
        primary_key=True),
    db.Column(
        'acl_id',
        db.Integer,
        db.ForeignKey('tbl_vsppm_acl.id'),
        primary_key=True))


class VSUser(CRUDMixin, db.Model):
    """"
    账户模型
    """
    __tablename__ = 'tbl_vsppm_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 账户名称
    username = db.Column(db.String(20), nullable=False, unique=True)
    # 邮箱
    email = db.Column(db.String(128), nullable=False, unique=True)
    # 手机号码
    mobile = db.Column(db.String(11))
    # 密码
    password = db.Column(db.String(60), nullable=False)
    # 真实姓名
    real_name = db.Column(db.String(100), nullable=False)
    # 头像
    avatar = db.Column(db.String(256))
    # 公司id
    company_id = db.Column(db.Integer,
                              db.ForeignKey('tbl_vsppm_company.id'))
    # 部门id
    department_id = db.Column(db.Integer,
                              db.ForeignKey('tbl_vsppm_department.id'))
    # 角色id
    role_id = db.Column(db.Integer,
                              db.ForeignKey('tbl_vsppm_role.id'))
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

    # 第一个参数为你要关系到哪个模型的名字,也就是类名
    # db.backref('users')第一个参数users为要反向引用的名字,也可以用其他名字
    # 正向引用是VSUser访问VSCompany,反向引用是从VSCompany访问表VSUser
    company = db.relationship('VSCompany', backref=db.backref('users'))

    # 第一个参数为你要关系到哪个模型的名字,也就是类名
    # db.backref('users')第一个参数users为要反向引用的名字,也可以用其他名字
    # 正向引用是VSUser访问VSDepartment,反向引用是从VSDepartment访问表VSUser
    department = db.relationship('VSDepartment', backref=db.backref('users'))

    # 让VSUser和VSRole产生关联
    # 因为VSUser和VSRole表中间还有一个vsppm_user_role表,所以添加secondary
    # 正向引用是VSUser访问VSRole,反向引用是从VSRole访问表VSUser
    role = db.relationship(
        'VSRole',
        backref=db.backref('users'))

    def __init__(self, password, **kwargs):
        super(VSUser, self).__init__(**kwargs)
        self.set_password(password)

    def __repr__(self):
        return '<VSUser #%s:%r>' % (self.id, self.username)

    def set_password(self, password):
        hash_ = bcrypt.generate_password_hash(password, 10).decode('utf-8')
        self.password = hash_

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def generate_token(self):
        """"
            :return
            bool: function exec result
            str: function exec data
        """
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=36000),
            'iat': datetime.datetime.utcnow(),
            'iss': 'ken',
            'data': {
                'username': self.username,
                'password': self.password
            }
        }

        return JwtEncoder().encoder(payload=payload)


class VSCompany(CRUDMixin, db.Model):
    """
    公司模型
    """
    __tablename__ = 'tbl_vsppm_company'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 公司名称
    name = db.Column(db.String(128), nullable=False, unique=True)
    # 公司负责人
    admin = db.Column(db.String(60))
    # 主页
    website = db.Column(db.String(128))

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

    def __init__(self, **kwargs):
        super(VSCompany, self).__init__(**kwargs)

    def __repr__(self):
        return '<VSCompany #%s:%r>' % (self.id, self.name)


class VSDepartment(CRUDMixin, db.Model):
    """
    部门模型
    """
    __tablename__ = 'tbl_vsppm_department'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 部门名称
    name = db.Column(db.String(128), nullable=False, unique=True)
    # 部门负责人
    admin = db.Column(db.String(60))
    # 所属公司id
    company_id = db.Column(db.Integer, nullable=False)

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

    def __init__(self, **kwargs):
        super(VSDepartment, self).__init__(**kwargs)

    def __repr__(self):
        return '<VSDepartment #%s:%r>' % (self.id, self.name)


class VSGroup(CRUDMixin, db.Model):
    """
    组模型
    """
    __tablename__ = 'tbl_vsppm_group'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 组名称
    name = db.Column(db.String(128), nullable=False, unique=True)
    # 组负责人
    admin = db.Column(db.String(60))
    # 所属部门id
    department_id = db.Column(db.Integer, nullable=False)

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

    def __init__(self, **kwargs):
        super(VSGroup, self).__init__(**kwargs)

    def __repr__(self):
        return '<VSGroup #%s:%r>' % (self.id, self.name)


class VSRole(CRUDMixin, db.Model):
    """
    角色模型
    """
    __tablename__ = 'tbl_vsppm_role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 角色名称
    name = db.Column(db.String(128), nullable=False, unique=True)
    # 角色描述
    role = db.Column(db.String(128), nullable=False)
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

    # 让VSRole和VSAcl产生关联
    # 因为VSAcl和VSRole表中间还有一个vsppm_user_role表,所以添加secondary
    # 正向引用是VSRole访问VSAcl,反向引用是从VSAcl访问表VSRole
    acls = db.relationship(
        'VSAcl',
        secondary=vsppm_role_acl,
        backref=db.backref('roles'))

    def __init__(self, **kwargs):
        super(VSRole, self).__init__(**kwargs)

    def __repr__(self):
        return '<VSRole #%s:%r>' % (self.id, self.name)


class VSAcl(CRUDMixin, db.Model):
    """
    权限模型
    """
    __tablename__ = 'tbl_vsppm_acl'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 权限模块名称
    module = db.Column(db.String(128), nullable=False)
    # 权限模块功能方法名称
    method = db.Column(db.String(128), nullable=False)
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

    def __init__(self, **kwargs):
        super(VSAcl, self).__init__(**kwargs)

    def __repr__(self):
        return '<VSAcl #%s:%r:%r>' % (self.id, self.module, self.method)
