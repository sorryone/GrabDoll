# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.formation_action import FormationAction
from grabDoll.action.user_action import UserAction
from grabDoll.action.item_action import ItemAction
import random
import time
__author__ = 'du_du'


def fight_against(uid, opponent):
    user_action = UserAction(uid)
    # 体力的扣除
    cur_vit = user_action.get_vit()
    cost_vit = 1
    if cur_vit < cost_vit:
        return False
    if user_action.reduce_vit(cost_vit) is False:
        return False

    my_formation = FormationAction(uid)
    opponent_formation = FormationAction(opponent)
    my_atk = my_formation.get_fight_atk()
    opponent_atk = opponent_formation.get_fight_atk()
    res = dict()
    res['my_atk'] = my_atk
    res['opponent_atk'] = opponent_atk
    award_success_gold = 10
    award_fail_gold = 2
    award = dict()
    award_success_items = [20010, 20011, 20012, 20013, 20014, 20015, 20016, 20017, 20018, 20019]
    item_action = ItemAction(uid)
    if my_atk > opponent_atk:
        result = True
        award_item = random.choice(award_success_items)
        award_item_ct = 1
        if item_action.add_model(award_item, award_item_ct):
            award[award_item] = award_item_ct
        if user_action.add_gold(award_success_gold):
            award['gold'] = award_success_gold

    else:
        result = False
        if user_action.add_gold(award_fail_gold):
            award['gold'] = award_fail_gold
    res['award'] = award
    res['result'] = result
    return res


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
    else:
        result = False
    res['award'] = award
    res['result'] = result
    return res
