# -*- coding: utf-8 -*-
from grabDoll.action.formation_action import FormationAction
from grabDoll.action.user_action import UserAction
from grabDoll.action.item_action import ItemAction
from grabDoll.action.hero_action import HeroAction
from grabDoll.action.mail_action import MailAction
from grabDoll.logics import artifact_logic
from grabDoll.logics import record_logic
import random
import time
import math
__author__ = 'du_du'


def fight_against(uid, opponent):
    if opponent == 'VIP':
        return guild_attack(uid)
    my_formation = FormationAction(uid)
    my_formation_info = my_formation.get_model_info()
    opponent_formation = FormationAction(opponent)
    opponent_info = opponent_formation.get_model_info()
    my_atk = my_formation_info.get(opponent_formation.fight_atk_str, 0)
    opponent_atk = opponent_info.get(opponent_formation.fight_atk_str, 10000)
    my_art_info = artifact_logic.get_artifact_akt(uid)
    opponent_art_info = artifact_logic.get_artifact_akt(opponent)
    res = dict()
    res['my_atk'] = my_atk + my_art_info.get('atk', 0)
    res['opponent_atk'] = opponent_atk + opponent_art_info.get('atk', 0)
    my_fight_heroes = my_formation_info.get(my_formation.fight_formation_str)
    my_fight_heroes_group = [i for i in my_fight_heroes if i != '']

    if eat_atk(uid, my_fight_heroes_group, res['opponent_atk']) is False:
        # 我受伤了已经
        res['error'] = True
        res['update'] = my_formation_info
    elif False:
        # elif opponent_info.get(opponent_formation.fight_state_str) == opponent_formation.state_injured:
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


def guild_attack(uid):
    res = dict()
    user_action = UserAction(uid)
    # 体力的扣除
    cur_vit = user_action.get_vit()
    cost_vit = 1
    if cur_vit < cost_vit:
        return False
    if user_action.reduce_vit(cost_vit) is False:
        return False
    award = dict()
    item_action = ItemAction(uid)
    result = True
    award_item = 20010
    award_item_ct = 1
    if item_action.add_model(award_item, award_item_ct):
        award[award_item] = award_item_ct
    res['award'] = award
    res['result'] = result
    return res


def eat_atk(uid, heroes_group, atk):
    hero_action = HeroAction(uid)
    heroes_info = hero_action.get_model_info()
    check_hero_group = [hero for hero_id, hero in heroes_info.items()
                        if hero_id in heroes_group and hero.get('hp', -1) > 0]
    hero_ct = len(check_hero_group)
    if hero_ct == 0:
        return False
    share_atk = math.floor(float(atk) / hero_ct)
    print hero_ct, share_atk
    for hero in check_hero_group:
        hero_action.injure_doll_hp(hero.get(hero_action.doll_id_str, 0), share_atk)
    return check_hero_group


def catch(uid, opponent):
    if opponent == 'VIP':
        return guild_catch(uid)
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
        record_logic.add_record(uid, 'rob', 1)
        mail_action = MailAction(opponent)
        mail_action.add_fight_message(uid)
    else:
        result = False
    res['award'] = award
    res['result'] = result
    return res


def guild_catch(uid):
    award = dict()
    res = dict()
    gold = 100
    user_action = UserAction(uid)
    user_action.add_gold(gold)
    award['gold'] = gold
    res['award'] = award
    res['result'] = True
    return res
