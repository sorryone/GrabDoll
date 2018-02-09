# -*- coding: utf-8 -*-
from grabDoll.action.user_action import UserAction
from grabDoll.action.pve_action import PveAction
from grabDoll.action.hatch_action import HatchAction
from grabDoll.action.friend_action import FriendAction
from grabDoll.action.record_action import RecordAction
from grabDoll.action.task_action import TaskAction
from grabDoll.action.mail_action import MailAction
from grabDoll.action.artifact_action import ArtifactAction
from grabDoll.action.book_action import HandBookAction
from grabDoll.action.formation_action import FormationAction
__author__ = 'du_du'


# 清空用户的数据
def clear_user_data(uid):
    u_action = UserAction(uid)
    hatch_action = HatchAction(uid)
    p_action = PveAction(uid)
    fri_action = FriendAction(uid)
    rec_action = RecordAction(uid)
    task_action = TaskAction(uid)
    mail_action = MailAction(uid)
    art_action = ArtifactAction(uid)
    book_action = HandBookAction(uid)
    formation_action = FormationAction(uid)
    res = {
        'user': u_action.remove(''),
        'hatch': hatch_action.remove(''),
        'pve': p_action.remove(''),
        'friend': fri_action.remove(''),
        'record': rec_action.remove(''),
        'task': task_action.remove(''),
        'mail': mail_action.remove(''),
        'artifact': art_action.remove(''),
        'book': book_action.remove(''),
        'formation': formation_action.remove(''),
    }
    return res
