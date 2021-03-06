# -*- coding: utf-8 -*-

import json
from lib.djhelper.api_view import api_render, api_view, api_result
from grabDoll.logics import user as user_logic
from grabDoll.logics import game_logic as game_logic
__author__ = 'maxijie'


@api_view(["GET"])
@api_result
def get_user_data(request):
    if request.method == "GET":
        try:
            print('get_user_data', 'user')
            uid = request.query_params.get('openid').encode('utf-8')
            open_key = request.query_params.get('openkey').encode('utf-8')
            platform = int(request.query_params.get('platform'))
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = game_logic.get_user_data(uid, open_key, platform)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def get_user_test(request):
    if request.method == "GET":
        try:
            print('get_user_data', 'user')
            uid = request.query_params.get('openid').encode('utf-8')
            open_key = request.query_params.get('openkey').encode('utf-8')
            platform = int(request.query_params.get('platform'))
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = game_logic.get_user_test(uid, open_key, platform)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


