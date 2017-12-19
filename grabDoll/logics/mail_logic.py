# -*- coding: utf-8 -*-
from grabDoll.action.mail_action import MailAction
from grabDoll.logics import inventory_logic
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
    if mail_info.get(action.read_str, True):
        return False
    award_json = mail_info.get(action.award_str)
    award = eval(award_json)
    if len(award) < 0:
        return False
    if action.mark_read(mail_id) is False:
        return False
    return inventory_logic.add_awards(award)

