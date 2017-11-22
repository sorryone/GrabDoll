# -*- coding: utf-8 -*-
from grabDoll.models.config_model import ConfigModel
from grabDoll.action.formation_action import FormationAction
from grabDoll.action.user_action import UserAction
__author__ = 'du_du'


def fight_against(uid, opponent):
    my_formation = FormationAction(uid)
    opponent_formation = FormationAction(opponent)
    my_atk = my_formation.get_fight_atk()
    opponent_atk = opponent_formation.get_fight_atk()
    res = dict()
    res['my_atk'] = my_atk
    res['opponent_atk'] = opponent_atk
    if my_atk > opponent_atk:
        res['result'] = True
    else:
        res['result'] = False
    return res


