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
from grabDoll.action.item_action import ItemAction
from grabDoll.action.hero_action import HeroAction
__author__ = 'du_du'


# 清空用户的数据
def clear_user_data(uid):
    u_action = UserAction(uid)
    hatch_action = HatchAction(uid)
    p_action = PveAction(uid)
    fri_action = FriendAction(uid)
    item_action = ItemAction(uid)
    hero_action = HeroAction(uid)
    rec_action = RecordAction(uid)
    task_action = TaskAction(uid)
    mail_action = MailAction(uid)
    art_action = ArtifactAction(uid)
    book_action = HandBookAction(uid)
    formation_action = FormationAction(uid)

    fri_keys = fri_action.get_keys()
    for fri_id in fri_keys:
        fri_action.remove(fri_id),
        print('remove friend', fri_id)

    item_keys = item_action.get_keys()
    for item_id in item_keys:
        item_action.remove(item_id),
        print('remove item', item_id)

    hero_keys = hero_action.get_keys()
    for hero_id in hero_keys:
        hero_action.remove(hero_id),
        print('remove hero', hero_id)

    res = {
        'user': u_action.remove(''),
        'hatch': hatch_action.remove(''),
        'pve': p_action.remove(''),
        'record': rec_action.remove(''),
        'task': task_action.remove(''),
        'mail': mail_action.remove(''),
        'artifact': art_action.remove(''),
        'book': book_action.remove(''),
        'formation': formation_action.remove(''),
    }
    return res
