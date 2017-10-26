# -*- coding: utf-8 -*-
import json
import time
from lib.platform.tencent_sdk_302.openapi_v3 import OpenAPIV3
from grabDoll.models.platform_model import PlatformModel
from grabDoll.models.user import User
__author__ = 'du_du'

appid = 1106233605
appkey = 'STwl4MAK67bcemOd'
iplist = ('openapi.sparta.html5.qq.com',)


def get_user_info_by_platform(openid, openkey):

    if openid == 'VIP' and openkey == 'VIP':
        print("IS VIP")
        model = PlatformModel(openid)
        return model.get_model_info()
    print("NOT VIP")
    set_up_info = is_setup(openid, openkey)
    user_info = get_info(openid, openkey)
    if type(set_up_info) is str or type(set_up_info) is object:
        set_up_info = eval(set_up_info)
    if type(user_info) is str or type(user_info) is object:
        user_info = eval(user_info)
    if set_up_info['ret'] != 0 or user_info['ret'] != 0:
        return False

    print("Start Dict")
    print(set_up_info)
    print(user_info)
    res = dict()
    if set_up_info['setuped'] == 1:
        print("a new user enter game")
        # 记录新用户的注册时间
        res['create_time'] = time.time()

    canshu_group = ('nickname', 'gender', 'country', 'province', 'city', 'figureurl', 'openid', 'qq_level', 'qq_vip_level')
    for canshu in canshu_group:
        if canshu in user_info:
            res[canshu] = user_info[canshu]
    res['login_time'] = time.time()
    print(res)
    model = PlatformModel(openid)
    model.set_values(res)
    print('return value')
    return res


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


