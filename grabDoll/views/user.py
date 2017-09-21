# -*- coding: utf-8 -*-

import json
from lib.djhelper.api_view import api_render, api_view, api_result
from grabDoll.logics import user as user_logic
from grabDoll.logics import game_logic as game_logic
__author__ = 'maxijie'


@api_view(["GET"])
@api_result
def set_user(request):
    if request.method == "GET":
        try:
            gold = int(request.query_params.get("gold"))
            uid = int(request.query_params.get('uid'))
            exp = int(request.query_params.get('exp'))
        except Exception as e:
            print(e)
            return 1, "参数错误"
    data = {
        "gold": gold,
        "uid": uid,
        "exp": exp,
    }
    if user_logic.set_userinfo(uid, data):
        return 0, data
    else:
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def get_user(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
        except Exception as e:
            print(e)
            return 1, "参数错误"

    try:
        data = game_logic.get_game_info(uid)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


