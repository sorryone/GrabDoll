# -*- coding: utf-8 -*-
import json
import time
from lib.platform.tencent_sdk_302.openapi_v3 import OpenAPIV3
from grabDoll.models.platform_model import PlatformModel
__author__ = 'du_du'

appid = 1106423014
appkey = 'PSqsIO5GwAu4wUL4'
iplist = ('openapi.sparta.html5.qq.com',)


def get_user_info_by_platform(openid, openkey):

    set_up_info = is_setup(openid, openkey)
    user_info = get_info(openid, openkey)
    set_data = eval(set_up_info)
    user_data = eval(user_info)
    if set_data['ret'] != 0 or user_info['ret'] != 0:
        return False

    res = dict()
    if set_data['setuped'] == 1:
        print("a new user enter game")
        # 记录新用户的注册时间
        res['create_time'] = time.time()
    res['data'] = user_data['data']
    res['login_time'] = time.time()
    model = PlatformModel(openid)
    model.set_values(res)
    return True


def get_info(openid, openkey):
    api = OpenAPIV3(appid, appkey, iplist)
    pf = 'qzone'
    j_data = api.call('/v3/user/get_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    return j_data


def is_setup(openid, openkey):
    api = OpenAPIV3(appid, appkey, iplist)
    pf = 'qzone'
    j_data = api.call('/v3/user/is_setup', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    return j_data


