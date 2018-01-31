# -*- coding: utf-8 -*-
import json
import time
from lib.platform.tencent_sdk_302.openapi_v3 import OpenAPIV3
from grabDoll.action.platform_action import PlatformAction
__author__ = 'du_du'

appid = 1106233605
appkey = 'STwl4MAK67bcemOd'
iplist = ('api.urlshare.cn',)
pf = 'wanba_ts'     # qzone


def get_user_info_by_platform(openid, openkey, platform):
    set_up_info = is_setup(openid, openkey)
    user_info = get_info(openid, openkey)
    if type(set_up_info) is str or type(set_up_info) is object:
        set_up_info = eval(set_up_info)
    if type(user_info) is str or type(user_info) is object:
        user_info = eval(user_info)
    if set_up_info['ret'] != 0 or user_info['ret'] != 0:
        return False
    res = dict()
    if set_up_info['setuped'] == 1:
        print("a new user enter game")
        # 记录新用户的注册时间
        res['create_time'] = time.time()
    else:
        print("old user enter game")
    canshu_group = ('nickname', 'gender', 'country', 'province', 'city', 'figureurl', 'openid', 'qq_level', 'qq_vip_level')
    for canshu in canshu_group:
        if canshu in user_info:
            res[canshu] = user_info[canshu]
    res['login_time'] = time.time()
    print(res)
    action = PlatformAction(openid)
    action.set_values(res)
    return res


def get_info(openid, openkey):
    api = OpenAPIV3(appid, appkey, iplist)
    j_data = api.call('/v3/user/get_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    return j_data


# 获取推荐的好友列表
def get_app_friends(openid, openkey):
    api = OpenAPIV3(appid, appkey, iplist)
    j_data = api.call('/v3/relation/get_app_friends', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    return j_data


# 这个接口需要申请
def get_rcmd_friends(openid, openkey):
    api = OpenAPIV3(appid, appkey, iplist)
    j_data = api.call('/v3/relation/get_rcmd_friends', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    return j_data


def is_friend(openid, openkey, fopenid):
    api = OpenAPIV3(appid, appkey, iplist)
    j_data = api.call('v3/relation/is_friend', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenid': fopenid
    })
    return j_data


def add_pal(openid, openkey):
    api = OpenAPIV3(appid, appkey, iplist)
    j_data = api.call('fusion2.dialog.addPal', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    return j_data


def is_setup(openid, openkey):
    api = OpenAPIV3(appid, appkey, iplist)
    j_data = api.call('/v3/user/is_setup', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    return j_data


