# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.formation_action import FormationAction
from grabDoll.action.user_action import UserAction
from grabDoll.action.item_action import ItemAction
from grabDoll.action.hero_action import HeroAction
from grabDoll.models.config_model import ConfigModel
from grabDoll.logics import artifact_logic
from grabDoll.logics import task_logic
import random
import time
__author__ = 'du_du'


def fight_against(uid, opponent):
    my_formation = FormationAction(uid)
    my_formation_info = my_formation.get_model_info()
    opponent_formation = FormationAction(opponent)
    opponent_info = opponent_formation.get_model_info()
    my_atk = my_formation_info.get(opponent_formation.fight_atk_str)
    opponent_atk = opponent_info.get(opponent_formation.fight_atk_str)
    my_art_info = artifact_logic.get_artifact_akt(uid)
    opponent_art_info = artifact_logic.get_artifact_akt(opponent)
    res = dict()
    res['my_atk'] = my_atk + my_art_info.get('atk', 0)
    res['opponent_atk'] = opponent_atk + opponent_art_info.get('atk', 0)
    my_fight_heroes = my_formation_info.get(my_formation.fight_formation_str)
    my_fight_heroes_group = [i for i in my_fight_heroes if i != '']
    print(my_fight_heroes_group)
    eat_atk(uid, my_fight_heroes_group, res['opponent_atk'])
    if my_formation_info.get(my_formation.fight_state_str) == my_formation.state_injured:
        # 我受伤了已经
        res['error'] = True
        res['update'] = my_formation_info
    elif opponent_info.get(opponent_formation.fight_state_str) == opponent_formation.state_injured:
        # 对方受伤了已经
        res['error'] = True
        res['update'] = opponent_info
    else:
        user_action = UserAction(uid)
        # 体力的扣除
        cur_vit = user_action.get_vit()
        cost_vit = 1
        if cur_vit < cost_vit:
            return False
        if user_action.reduce_vit(cost_vit) is False:
            return False
        award_success_gold = 10
        award_fail_gold = 2
        award = dict()
        award_success_items = [20010, 20011, 20012, 20013, 20014, 20015, 20016, 20017, 20018, 20019]
        item_action = ItemAction(uid)
        if my_atk > opponent_atk:
            result = True
            opponent_formation.set_injured()
            award_item = random.choice(award_success_items)
            award_item_ct = 1
            if item_action.add_model(award_item, award_item_ct):
                award[award_item] = award_item_ct
            if user_action.add_gold(award_success_gold):
                award['gold'] = award_success_gold
        else:
            result = False
            my_formation.set_injured()
            if user_action.add_gold(award_fail_gold):
                award['gold'] = award_fail_gold
        res['award'] = award
        res['result'] = result
    return res


def eat_atk(uid, heroes_group, atk):
    hero_action = HeroAction(uid)
    heroes_info = hero_action.get_model_info()
    return heroes_info


def catch(uid, opponent):
    award = dict()
    res = dict()
    opponent_formation = FormationAction(opponent)
    user_action = UserAction(uid)
    opponent_formation_info = opponent_formation.get_model_info()
    cur_income = opponent_formation_info.get(opponent_formation.income_str, 0)
    catch_ct = opponent_formation_info.get(opponent_formation.catch_ct_str, 0)
    catch_refresh_time = opponent_formation_info.get(opponent_formation.catch_refresh_time_str, 0)
    cur_time = int(time.time())
    catch_cd = 600
    if cur_time < catch_refresh_time + catch_cd:
        # 时间不到需要等待
        return False
    update_data = dict()
    update_data[opponent_formation.catch_refresh_time_str] = cur_time
    update_data[opponent_formation.catch_ct_str] = catch_ct + 1
    gold = int(cur_income / 10)
    update_data[opponent_formation.income_str] = cur_income - gold
    if opponent_formation.set_model_info(update_data):
        user_action.add_gold(gold)
        print('gold', gold)
        award['gold'] = gold
        res['update'] = update_data
        result = True
        task_logic.update_task_info(uid, 'rob', 0, 1)
    else:
        result = False
    res['award'] = award
    res['result'] = result
    return res
