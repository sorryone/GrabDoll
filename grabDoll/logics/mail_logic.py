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
    award_res = inventory_logic.add_awards(uid, award)
    res = {
        'key_id': mail_id,
        'award': award_res,
    }
    return res


def delete_all_mail(uid):
    action = MailAction(uid)
    remove_result = action.remove_scrap_mails()
    if remove_result is False:
        return False
    elif isinstance(remove_result, (list, )):
        mail_id_list = [str(mail[action.key_str]) for mail in remove_result]
    else:
        print('type', type(remove_result))
        mail_id_list = [remove_result[action.key_str]]
    print('mail_id_list', mail_id_list)
    return mail_id_list


def get_all_mail_award(uid):
    action = MailAction(uid)
    # 拿到未读的
    mail_list = action.get_need_award_mails()
    if len(mail_list) < 0:
        return False
    awards = [eval(mail.get(action.award_str)) for mail in mail_list]
    print(awards)
    all_awards = union_dict(awards)
    mark_result = action.mark_read_group()
    print('remove_result', mark_result)
    award_res = inventory_logic.add_awards(uid, all_awards)
    res = {
        'award': award_res,
    }
    return res


def union_dict(data_group):
    _keys = set(sum([obj.keys() for obj in data_group], []))
    _total = {}
    for _key in _keys:
        _total[_key] = sum([obj.get(_key, 0) for obj in data_group])
    return _total
