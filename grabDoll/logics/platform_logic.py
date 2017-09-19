# -*- coding: utf-8 -*-
import json
from lib.platform.tencent_sdk_302.openapi_v3 import OpenAPIV3
__author__ = 'du_du'

appid = 1106423014
appkey = 'PSqsIO5GwAu4wUL4'
iplist = ('openapi.sparta.html5.qq.com',)


def get_info(openid, openkey):

    openid = '000000000000000000000000199B6A55'
    openkey = '84BAEDACC5B512FE914C8192E5DC591A'
    print('openid', openid)
    print('openkey', openkey)
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


