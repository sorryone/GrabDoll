# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.formation_action import FormationAction
from grabDoll.action.user_action import UserAction
from grabDoll.action.item_action import ItemAction
import random
__author__ = 'du_du'


def fight_against(uid, opponent):
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
    user_action = UserAction(uid)
    item_action = ItemAction(uid)
    if my_atk > opponent_atk:
        res['result'] = True
        award_item = random.choice(award_success_items)
        award_item_ct = 1
        if item_action.add_model(award_item, award_item_ct):
            award[award_item] = award_item_ct
        if user_action.add_gold(award_success_gold):
            award['gold'] = award_success_gold

    else:
        res['result'] = False
        if user_action.add_gold(award_fail_gold):
            award['gold'] = award_fail_gold
    return res


