# -*- coding: utf-8 -*-
import json
from lib.djhelper.api_view import api_render, api_view, api_result
from grabDoll.logics import mail_logic as mail_logic
__author__ = 'du_du'


@api_view(["GET"])
@api_result
def get_mail_award(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
            mail_id = str(request.query_params.get('mail_id'))
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = mail_logic.get_mail_award(uid, mail_id)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def delete_all_mail(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = mail_logic.delete_all_mail(uid)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"


@api_view(["GET"])
@api_result
def get_all_mail_award(request):
    if request.method == "GET":
        try:
            uid = request.query_params.get('uid')
        except Exception as e:
            print(e)
            return 1, "参数错误"
    try:
        data = mail_logic.get_all_mail_award(uid)
        return 0, data
    except Exception as e:
        print(e)
        return 1, "数据错误"
