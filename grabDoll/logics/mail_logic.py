# -*- coding: utf-8 -*-
from grabDoll.action.mail_action import MailAction
__author__ = 'du_du'


def get_mail_info(uid):
    action = MailAction(uid)
    res = action.get_model_info()
    return res

