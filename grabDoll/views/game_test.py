# -*- coding: utf-8 -*-
__author__ = 'dudu'

import json
from lib.djhelper.api_view import api_render, api_view, api_result
from grabDoll.logics import platform_logic as platform_logic


@api_view(["GET"])
@api_result
def get_info(request):
    if request.method == "GET":
        try:
            print(request.query_params)
            openid = request.query_params.get('openid')
            openkey = request.query_params.get('openkey')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = platform_logic.get_info(openid, openkey)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"




