# -*- coding: utf-8 -*-
import json
from lib.djhelper.api_view import api_render, api_view, api_result
from grabDoll.logics import friend_logic as friend_logic
__author__ = 'du_du'


@api_view(["POST"])
@api_result
def get_my_friend_info(request):
    if request.method == "POST":
        try:
            print(request.query_params)
            uid = request.query_params.get('uid')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = friend_logic.get_my_friend_info(uid)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["POST"])
@api_result
def enter_friend_home(request):
    if request.method == "POST":
        try:
            print(request.query_params)
            uid = request.query_params.get('uid')
            friend_id = request.query_params.get('friend_id')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = friend_logic.enter_friend_home(uid, friend_id)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["POST"])
@api_result
def add_friend(request):
    if request.method == "POST":
        try:
            print(request.query_params)
            uid = request.query_params.get('uid')
            friend_id = request.query_params.get('friend_id')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = friend_logic.add_friend(uid, friend_id)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["POST"])
@api_result
def accept_friend(request):
    if request.method == "POST":
        try:
            print(request.query_params)
            uid = request.query_params.get('uid')
            friend_id = request.query_params.get('friend_id')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = friend_logic.accept_friend(uid, friend_id)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["POST"])
@api_result
def refuse_friend(request):
    if request.method == "POST":
        try:
            print(request.query_params)
            uid = request.query_params.get('uid')
            friend_id = request.query_params.get('friend_id')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = friend_logic.refuse_friend(uid, friend_id)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["POST"])
@api_result
def remove_friend(request):
    if request.method == "POST":
        try:
            print(request.query_params)
            uid = request.query_params.get('uid')
            friend_id = request.query_params.get('friend_id')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = friend_logic.remove_friend(uid, friend_id)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["POST"])
@api_result
def rob_money(request):
    if request.method == "POST":
        try:
            print(request.query_params)
            uid = request.query_params.get('uid')
            friend_id = request.query_params.get('friend_id')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = friend_logic.rob_money(uid, friend_id)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["POST"])
@api_result
def rob_doll(request):
    if request.method == "POST":
        try:
            print(request.query_params)
            uid = request.query_params.get('uid')
            friend_id = request.query_params.get('friend_id')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = friend_logic.rob_doll(uid, friend_id)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"

