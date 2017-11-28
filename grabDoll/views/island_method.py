# -*- coding: utf-8 -*-
from lib.djhelper.api_view import api_render, api_view, api_result
from grabDoll.logics import island_logic
__author__ = 'du_du'


@api_view(["GET"])
@api_result
def refresh_income_info(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = island_logic.refresh_income_info(uid)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def award_income(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = island_logic.award_income(uid)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"
