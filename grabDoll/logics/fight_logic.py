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
    all_atk = 0
    hero_config = ConfigModel('doll')
    hero_upgrade_config = ConfigModel('doll_upgrade')
    fight_heroes = formation_action.get_fight_model_info()
    heroes = hero_action.get_model_info()
    normal_per = 0.1
    fight_per = 0.9

    for hero_id, hero_info in heroes.iteritems():
        cur_hero_config = hero_config.get_config_by_id(hero_id)
        cur_lv_config = hero_upgrade_config.get_config_by_id(70000 + int(hero_info['lv']))
        base_atk = int(cur_hero_config['atk'])
        add = int(cur_lv_config['add'])
        hero_atk = base_atk * add
        # print(hero_id, hero_atk, base_atk, add)
        if hero_id in fight_heroes:
            all_atk += hero_atk * fight_per
        else:
            all_atk += hero_atk * normal_per
    return all_atk


def fight_against(uid, opponent):
    my_atk = get_atk(uid)
    opponent_atk = get_atk(opponent)
    res = dict()
    res['my_atk'] = my_atk
    res['opponent_atk'] = opponent_atk
    if my_atk > opponent_atk:
        res['result'] = True
    else:
        res['result'] = False
    return res


