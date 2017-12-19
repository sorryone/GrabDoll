# -*- coding: utf-8 -*-
from grabDoll.action.mail_action import MailAction
__author__ = 'du_du'


def get_mail_info(uid):
    action = MailAction(uid)
    res = action.get_model_info()
    return res


def add_lv_up_award(uid):
    action = MailAction(uid)
    award = {'gold': 100, 'diamond': 10}
    return action.add_lv_up_award(award)


def get_mail_award(uid, mail_id):
    action = MailAction(uid)
    mail_info = action.get_model_info_by_id(mail_id)
    return mail_info

