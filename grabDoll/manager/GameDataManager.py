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
from grabDoll.action.note_action import NoteAction
from grabDoll.action.machine_action import MachineAction
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
    note_action = NoteAction(uid)
    mach_action = MachineAction(uid)
    print ('---------  START REMOVE FRIEND  -----------')
    fri_keys = fri_action.get_keys()
    for fri_id in fri_keys:
        fri_action.remove(fri_id),
        print('remove friend', fri_id)
    print ('---------  START REMOVE ITEM  -----------')
    item_keys = item_action.get_keys()
    for item_id in item_keys:
        item_action.remove(item_id),
        print('remove item', item_id)
    print ('---------  START REMOVE HERO  -----------')
    hero_keys = hero_action.get_keys()
    for hero_id in hero_keys:
        hero_action.remove(hero_id),
        print('remove hero', hero_id)

    print ('---------  START REMOVE BOOK  -----------')
    book_keys = book_action.get_keys()
    for book_id in book_keys:
        book_action.remove(book_id),
        print('remove book', book_id)

    print ('---------  START REMOVE NOTE  -----------')
    note_keys = note_action.cache.get_keys()
    for note_id in note_keys:
        note_action.cache.pop(note_id),
        print('remove note', note_id)

    print ('---------  START REMOVE MACHINE  -----------')
    mach_keys = mach_action.model.get_keys()
    for mach_id in mach_keys:
        mach_action.model.pop(mach_id),
        print('remove mach', mach_id)

    print ('---------  START REMOVE DB  -----------')

    res = {
        'user': u_action.remove(''),
        'hatch': hatch_action.remove(''),
        'pve': p_action.remove(''),
        'record': rec_action.remove(''),
        'task': task_action.remove(''),
        'mail': mail_action.remove(''),
        'artifact': art_action.remove(''),
        'formation': formation_action.remove(''),
    }
    return res
