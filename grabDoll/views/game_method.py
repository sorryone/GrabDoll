# -*- coding: utf-8 -*-
__author__ = 'dudu'

import json
from lib.djhelper.api_view import api_render, api_view, api_result
from grabDoll.logics import user as user_logic
from grabDoll.logics import inventory_logic as inventory_logic


@api_view(["GET"])
@api_result
def grab_egg(request):
    if request.method == "GET":
        try:
            print(request.query_params)
            uid = int(request.query_params.get('uid'))
            item_id = request.query_params.get('item_id')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = inventory_logic.use_item(uid, item_id)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def create_user(request):
    if request.method == "GET":
        try:
            print(request.query_params)
            uid = int(request.query_params.get('uid'))
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = user_logic.create_user(uid)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def speed_up(request):
    if request.method == "GET":
        try:
            print(request.query_params)
            uid = int(request.query_params.get('uid'))
            item_id = request.query_params.get('item_id')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = inventory_logic.gacha_speed_up(uid, item_id)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"




