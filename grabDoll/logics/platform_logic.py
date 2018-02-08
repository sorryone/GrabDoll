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


def get_user_info_by_platform(openid, open_key):
    # 判断是否已经登陆
    if check_login(openid, open_key) is False:
        return False
    action = PlatformAction(openid)
    p_info = action.get_model_info()
    if len(p_info) == 0:
        set_up_info = is_setup(openid, open_key)
        p_info = get_info(openid, open_key)
        if type(set_up_info) is str or type(set_up_info) is object:
            set_up_info = eval(set_up_info)
        if type(p_info) is str or type(p_info) is object:
            p_info = eval(p_info)
        if set_up_info['ret'] != 0 or p_info['ret'] != 0:
            return False
        res = dict()
        if set_up_info['setuped'] == 1:
            print("a new user enter game")
            # 记录新用户的注册时间
            res['create_time'] = time.time()
        else:
            print("old user enter game")
        key_group = ('nickname', 'gender', 'country', 'province', 'city', 'figureurl', 'openid', 'qq_level', 'qq_vip_level')
        for key_str in key_group:
            if key_str in p_info:
                res[key_str] = p_info[key_str]
        res['login_time'] = time.time()
        action.set_values(res)
        return res
    else:
        return p_info


def check_login(openid, open_key):
    res_data = is_login(openid, open_key)
    if type(res_data) is str or type(res_data) is object:
        res_data = eval(res_data)
    return res_data.get('ret', -1) == 0


def is_login(openid, openkey):
    api = OpenAPIV3(appid, appkey, iplist)
    j_data = api.call('/v3/user/is_login', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    return j_data


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


