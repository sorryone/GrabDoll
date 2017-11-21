# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.formation_action import FormationAction
from grabDoll.action.hero_action import HeroAction
from grabDoll.action.user_action import UserAction
__author__ = 'du_du'


# 获取用户的攻击数据
def get_atk(uid):
    formation_action = FormationAction(uid)
    hero_action = HeroAction(uid)
    atk = 0
    hero_config = ConfigModel('doll')
    hero_upgrade_config = ConfigModel('doll_upgrade')
    fight_heroes = formation_action.get_fight_model_info()
    heroes = hero_action.get_model_info()

    for hero_id, hero_info in heroes.iteritems():
        print hero_id
        print hero_info
    return atk


