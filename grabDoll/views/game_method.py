# -*- coding: utf-8 -*-
import json
from lib.djhelper.api_view import api_render, api_view, api_result
from grabDoll.logics import user as user_logic
from grabDoll.logics import inventory_logic as inventory_logic
from grabDoll.logics import game_logic as game_logic
from grabDoll.logics import machine_logic as machine_logic
from grabDoll.logics import shop_logic as shop_logic
from grabDoll.logics import hatch_logic as hatch_logic
from grabDoll.logics import artifact_logic as artifact_logic
__author__ = 'du_du'


@api_view(["POST"])
@api_result
def start_grab(request):
    if request.method == "POST":
        try:
            uid = request.data['uid']
            item_id = request.data['item_id']
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = machine_logic.start_grab(uid, item_id)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


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
            machine = request.query_params.get('machine')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = machine_logic.reset_machine(uid, machine)
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
            item_id = int(request.query_params.get('item_id'))
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
def hatch_unlock(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
            index = int(request.query_params.get('index'))
            if index is None:
                return 1, "错误索引"
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = hatch_logic.hatch_unlock(uid, index)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def hatch_speed(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
            index = int(request.query_params.get('index'))
            if index is None:
                return 1, "错误索引"
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = hatch_logic.hatch_speed(uid, index)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def hatch_open(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
            index = int(request.query_params.get('index'))
            if index is None:
                return 1, "错误索引"
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = hatch_logic.hatch_open(uid, index)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def hatch_discard(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
            index = int(request.query_params.get('index'))
            if index is None:
                return 1, "错误索引"
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = hatch_logic.hatch_discard(uid, index)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def upgrade_artifact(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
            artifact = int(request.query_params.get('artifact'))
            if artifact is None:
                return 1, "错误索引"
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = artifact_logic.upgrade_artifact(uid, artifact)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def buy_vit(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = user_logic.buy_vit(uid)
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




