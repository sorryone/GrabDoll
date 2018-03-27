# -*- coding: utf-8 -*-
from grabDoll.action.hero_action import HeroAction
import time
__author__ = 'du_du'


def interact_doll(uid, hero_id):
    action = HeroAction(uid)
    res = action.interact_doll(hero_id)
    return res
