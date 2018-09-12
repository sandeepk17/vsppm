#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask_mail import Message

from lib.extensions import mail, rq
from app.auth.models import VSUser


@rq.job
def send_registration_email(uid, token):
    """Sends a registratiion email to the given uid."""
    user = VSUser.query.filter_by(id=uid).first()
    msg = Message(
        'User Registration',
        sender='admin@flask-bones.com',
        recipients=[user.email]
    )
    msg.body = '<p>hello<p>'
    mail.send(msg)
