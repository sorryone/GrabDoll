# -*- coding: utf-8 -*-
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


def set_fight(uid, heroes):
    print (heroes)
    print type(heroes)
    action = FormationAction(uid)
    myHeroes = HeroAction(uid).get_keys()
    return action.set_fight_model_info(heroes)


def set_explore(uid, heroes):
    return True

if __name__ == "__main__":
    # print get_game_info('ED57884CAA078DF9E0E08750D98CA834', 'F7D770DA0E6E8BDC6FF1D0A652925E2B')
    print get_formation_info('VIP')

