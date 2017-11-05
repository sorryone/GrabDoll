# -*- coding: utf-8 -*-
import json
from lib.djhelper.api_view import api_render, api_view, api_result
from grabDoll.logics import user as user_logic
from grabDoll.logics import inventory_logic as inventory_logic
from grabDoll.logics import game_logic as game_logic
from grabDoll.logics import machine_logic as machine_logic
from grabDoll.logics import shop_logic as shop_logic
__author__ = 'du_du'


@api_view(["POST"])
@api_result
def grab_egg(request):
    if request.method == "POST":
        try:
            uid = request.data['uid']
            item_id = request.data['item_id']
            eggs = request.data['eggs']
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = machine_logic.grab_egg(uid, item_id, eggs)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def switch_machine(request):
    if request.method == "GET":
        try:
            print(request.query_params)
            uid = request.query_params.get('uid')
            machine = request.query_params.get('machine')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = machine_logic.switch_machine(uid, machine)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def reset_machine(request):
    if request.method == "GET":
        try:
            print(request.query_params)
            uid = request.query_params.get('uid')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = machine_logic.reset_machine(uid)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def buy_shop(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
            shop_id = request.query_params.get('shop_id')
            if shop_id is None:
                return 1, "未知的道具"
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = shop_logic.buy(uid, shop_id)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def use_item(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
            item_id = request.query_params.get('item_id')
            if item_id is None:
                return 1, "未知的道具"
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
def speed_up(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
            item_id = request.query_params.get('item_id')
            if item_id is None:
                return 1, "未知的道具"
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = inventory_logic.gacha_speed_up(uid, item_id)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def get_debug(request):
    if request.method == "GET":
        try:
            debug_info = str(request.query_params.get('debug'))
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        return 0, debug_info
    except Exception as e:
        print(e)
        return 1, "数据错误"




