# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.formation_action import FormationAction
from grabDoll.action.hero_action import HeroAction
__author__ = 'du_du'


def get_formation_info(uid):
    action = FormationAction(uid)
    return action.get_model_info()


def set_fight(uid, fight_heroes):
    formation_action = FormationAction(uid)
    check_heroes = [i for i in fight_heroes if i != '']
    # 判断有没有重复英雄
    if len(check_heroes) != len(set(check_heroes)):
        print('is same')
        return False
    hero_action = HeroAction(uid)
    all_hero = hero_action.get_model_info()
    # 有没有根本不存在的英雄
    if len(set(check_heroes) - set(all_hero.keys())) > 0:
        print('is not exist')
        return False
    # 读取英雄属性配置信息
    hero_config = ConfigModel('doll')
    hero_upgrade_config = ConfigModel('doll_upgrade')
    # 计算战斗力
    all_atk = 0
    all_capacity = 0
    normal_fight_per = 0.1
    fight_per = 0.9
    for hero_id, hero_info in all_hero.iteritems():
        cur_hero_config = hero_config.get_config_by_id(hero_id)
        cur_lv_config = hero_upgrade_config.get_config_by_id(70000 + int(hero_info['lv']))
        if int(cur_hero_config['category']) != formation_action.fight_type and hero_id in check_heroes:
            print('is not fight hero', hero_id)
            return False
        base_atk = int(cur_hero_config['atk'])
        base_capacity = int(cur_hero_config['capacity'])
        atk_add_per = int(cur_lv_config['add_atk'])
        capacity_add_per = int(cur_lv_config['add_capacity'])
        hero_atk = base_atk * atk_add_per
        hero_capacity = base_capacity * capacity_add_per
        if hero_id in fight_heroes:
            all_atk += hero_atk * fight_per
        else:
            all_atk += hero_atk * normal_fight_per
            all_capacity += hero_capacity
    info = formation_action.get_model_info()
    cur_income = info.get(formation_action.income_str)
    data = {
        formation_action.fight_formation_str: fight_heroes,
        formation_action.fight_atk_str: all_atk,
        formation_action.capacity_str: all_capacity,
    }
    print(fight_heroes)
    if formation_action.set_model_info(data):
        print(data)
        return data
    return False


def set_explore(uid, fight_heroes):
    formation_action = FormationAction(uid)
    check_heroes = [i for i in fight_heroes if i != '']
    # 判断有没有重复英雄
    if len(check_heroes) != len(set(check_heroes)):
        print('is same')
        return False
    hero_action = HeroAction(uid)
    all_hero = hero_action.get_model_info()
    # 有没有根本不存在的英雄
    if len(set(check_heroes) - set(all_hero.keys())) > 0:
        print('is not exist')
        return False
    info = formation_action.get_model_info()
    if len(set(check_heroes) & set(info.get(formation_action.explore_formation_str))) > 0:
        print('pve hero in fight formation')
        return False
    data = {
        formation_action.explore_formation_str: fight_heroes,
    }
    print(fight_heroes)
    if formation_action.set_model_info(data):
        print(data)
        return data
    return False


def get_pve_heroes_info(uid):
    for_action = FormationAction(uid)
    hero_action = HeroAction(uid)
    all_hero = hero_action.get_model_info()
    pve_heroes = for_action.get_explore_model_info()
    return {hero_id: hero_info for hero_id, hero_info in all_hero.items() if hero_id in pve_heroes}


if __name__ == "__main__":
    # print get_game_info('ED57884CAA078DF9E0E08750D98CA834', 'F7D770DA0E6E8BDC6FF1D0A652925E2B')
    print get_formation_info('VIP')

