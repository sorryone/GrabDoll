# -*- coding: utf-8 -*-
__author__ = 'dudu'

import json
from lib.djhelper.api_view import api_render, api_view, api_result
from grabDoll.logics import inventory_logic as inventory_logic

@api_view(["GET"])
@api_result
def get_inventory(request):
    if request.method == "GET":
        try:
            print(request.query_params)
            uid = int(request.query_params.get('uid'))
        except Exception as e:
            print(e)
            return 1, "参数错误"

    data = inventory_logic.get_item_info(uid)
    if(data):
        return 0, data
    else:
        return 1, "数据错误"