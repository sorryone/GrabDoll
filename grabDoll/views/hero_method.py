# -*- coding: utf-8 -*-
from lib.djhelper.api_view import api_render, api_view, api_result
from grabDoll.logics import hero_logic
__author__ = 'du_du'


@api_view(["GET"])
@api_result
def interact_doll(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
            hero_id = int(request.query_params.get('hero_id'))
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = hero_logic.interact_doll(uid, hero_id)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"

