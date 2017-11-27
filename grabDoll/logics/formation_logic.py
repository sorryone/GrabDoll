# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.formation_action import FormationAction
from grabDoll.action.hero_action import HeroAction
__author__ = 'du_du'


def get_formation_info(uid):
    action = FormationAction(uid)
    res = {
        'fight': action.get_fight_model_info(),
        'explore': action.get_explore_model_info(),
    }
    return res


def set_fight(uid, fight_heroes):
    formation_action = FormationAction(uid)
    check_heroes = [i for i in fight_heroes if i != '']
    # 判断有没有重复英雄
    if len(check_heroes) != len(set(check_heroes)):
        return False
    hero_action = HeroAction(uid)
    all_hero = hero_action.get_model_info()
    # 有没有根本不存在的英雄
    if len(set(check_heroes) - set(all_hero.keys())) > 0:
        return False
    # 读取英雄属性配置信息
    hero_config = ConfigModel('doll')
    hero_upgrade_config = ConfigModel('doll_upgrade')
    # 计算战斗力
    all_atk = 0
    normal_per = 0.1
    fight_per = 0.9
    for hero_id, hero_info in all_hero.iteritems():
        cur_hero_config = hero_config.get_config_by_id(hero_id)
        cur_lv_config = hero_upgrade_config.get_config_by_id(70000 + int(hero_info['lv']))
        base_atk = int(cur_hero_config['atk'])
        add = int(cur_lv_config['add'])
        hero_atk = base_atk * add
        if hero_id in fight_heroes:
            all_atk += hero_atk * fight_per
        else:
            all_atk += hero_atk * normal_per
    data = {
        formation_action.fight_formation_str: fight_heroes,
        formation_action.fight_atk_str: all_atk,
    }
    return formation_action.set_fight_model_info(data)


def set_explore(uid, heroes):
    return True

if __name__ == "__main__":
    # print get_game_info('ED57884CAA078DF9E0E08750D98CA834', 'F7D770DA0E6E8BDC6FF1D0A652925E2B')
    print get_formation_info('VIP')

