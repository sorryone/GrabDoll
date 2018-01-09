# -*- coding: utf-8 -*-
import json
from lib.djhelper.api_view import api_render, api_view, api_result
from grabDoll.logics import task_logic
__author__ = 'du_du'


@api_view(["GET"])
@api_result
def get_task_info(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = task_logic.get_task_info(uid)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def get_task_award(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
            task_id = int(request.query_params.get('task_id'))
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = task_logic.get_task_award(uid, task_id)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"