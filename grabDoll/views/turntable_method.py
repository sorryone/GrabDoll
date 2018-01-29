# -*- coding: utf-8 -*-
import json
from lib.djhelper.api_view import api_render, api_view, api_result
from grabDoll.logics import turntable_logic
__author__ = 'du_du'


@api_view(["GET"])
@api_result
def try_once(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = turntable_logic.try_once(uid)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def try_five_times(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = turntable_logic.try_five_times(uid)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"