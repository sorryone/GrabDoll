# -*- coding: utf-8 -*-
import json
from lib.djhelper.api_view import api_render, api_view, api_result
from grabDoll.logics import formation_logic
__author__ = 'du_du'


@api_view(["GET"])
@api_result
def set_fight(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
            heroes = str(request.query_params.get('list')).split(',')
            if heroes is None:
                return 1, "错误索引"
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = formation_logic.set_fight(uid, heroes)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def set_explore(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
            heroes = str(request.query_params.get('list')).split(',')
            if heroes is None:
                return 1, "错误索引"
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = formation_logic.set_explore(uid, heroes)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"