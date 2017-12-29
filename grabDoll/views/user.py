# -*- coding: utf-8 -*-

import json
from lib.djhelper.api_view import api_render, api_view, api_result
from grabDoll.logics import user as user_logic
from grabDoll.logics import game_logic as game_logic
__author__ = 'maxijie'


@api_view(["GET"])
@api_result
def get_user(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
            open_key = request.query_params.get('openkey')
            is_debug = request.query_params.get('isDebug')
        except Exception as e:
            print(e)
            return 1, "参数错误"

    try:
        data = game_logic.get_game_info(uid, open_key, is_debug)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def get_user_data(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
            open_key = request.query_params.get('openkey')
            is_debug = request.query_params.get('isDebug')
        except Exception as e:
            print(e)
            return 1, "参数错误"

    try:
        data = game_logic.get_user_data(uid, open_key, is_debug)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"

