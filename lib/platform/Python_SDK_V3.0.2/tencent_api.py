#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from openapi_v3 import OpenAPIV3

# 正式的
# appid = 1106233605
# appkey = 'STwl4MAK67bcemOd'
# 我自己的测试服务器
appid = 1106423014
appkey = 'PSqsIO5GwAu4wUL4'


iplist = ('172.27.0.91',)
# iplist = ('10.6.207.119:9191',)
# iplist = ('10.166.146.171',)
# iplist = ('10.166.146.174',)
# iplist = ('172.25.36.57:8191',)
# iplist = ('proxy.qq.com',)

# openid = ''
# openkey = ''
openid = '0000000000000000000000000039811C'
openkey = 'BAA4A7F86ABCE56A4FC98AD0B81FB542'


api = OpenAPIV3(appid, appkey, iplist)


def pretty_show(jdata):
    import json
    print json.dumps(jdata, indent=4, ensure_ascii=False).encode('utf8')


def qz_core_test():
    pf = 'qzone'

    jdata = api.call('/v3/user/get_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    jdata = api.call('/v3/relation/get_app_friends', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    openidlist = []
    if jdata['ret'] == 0:
        openidlist = [fid['openid'] for fid in jdata['items']]

    jdata = api.call('/v3/user/get_multi_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenids': '_'.join(openidlist)
    })
    pretty_show(jdata)

    jdata = api.call('/v3/user/is_setup', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    jdata = api.call('/v3/relation/is_friend', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenid': '0000000000000000000000000326E4AA'
    })
    pretty_show(jdata)

    jdata = api.call('/v3/user/get_rich_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    jdata = api.call('/v3/relation/get_all_friends', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)


def qp_core_test():
    pf = 'qplus'

    jdata = api.call('/v3/user/get_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    jdata = api.call('/v3/relation/get_app_friends', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    openidlist = []
    if jdata['ret'] == 0:
        openidlist = [fid['openid'] for fid in jdata['items']]

    jdata = api.call('/v3/user/get_multi_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenids': '_'.join(openidlist)
    })
    pretty_show(jdata)

    jdata = api.call('/v3/user/is_setup', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    jdata = api.call('/v3/relation/is_friend', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenid': '0000000000000000000000000326E4AA'
    })
    pretty_show(jdata)

    jdata = api.call('/v3/user/get_rich_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    jdata = api.call('/v3/relation/get_all_friends', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)


def py_core_test():
    pf = 'pengyou'

    jdata = api.call('/v3/user/get_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    jdata = api.call('/v3/relation/get_app_friends', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    openidlist = []
    if jdata['ret'] == 0:
        openidlist = [fid['openid'] for fid in jdata['items']]

    jdata = api.call('/v3/user/get_multi_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenids': '_'.join(openidlist)
    })
    pretty_show(jdata)

    jdata = api.call('/v3/user/is_setup', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    jdata = api.call('/v3/relation/is_friend', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenid': '0000000000000000000000000326E4AA'
    })
    pretty_show(jdata)

    jdata = api.call('/v3/user/get_rich_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    jdata = api.call('/v3/relation/get_all_friends', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)


def kx_core_test():
    pf = 'kapp'

    jdata = api.call('/v3/user/get_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    jdata = api.call('/v3/relation/get_app_friends', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    openidlist = []
    if jdata['ret'] == 0:
        openidlist = [fid['openid'] for fid in jdata['items']]

    jdata = api.call('/v3/user/get_multi_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenids': '_'.join(openidlist)
    })
    pretty_show(jdata)

    jdata = api.call('/v3/user/is_setup', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    jdata = api.call('/v3/relation/is_friend', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenid': '00000000000000010000000005881504'
    })
    pretty_show(jdata)


def manyou_core_test():
    pf = 'manyou100'

    jdata = api.call('/v3/user/get_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    jdata = api.call('/v3/relation/get_app_friends', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    openidlist = []
    if jdata['ret'] == 0:
        openidlist = [fid['openid'] for fid in jdata['items']]

    jdata = api.call('/v3/user/get_multi_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenids': '_'.join(openidlist)
    })
    pretty_show(jdata)

    jdata = api.call('/v3/user/is_setup', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    jdata = api.call('/v3/relation/is_friend', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenid': '00000000000000000000000007B673FF'
    })
    pretty_show(jdata)


def xingcloud_core_test():
    pf = 'xingcloud'

    jdata = api.call('/v3/user/is_login_xingcloud', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    jdata = api.call('/v3/user/get_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    jdata = api.call('/v3/relation/get_app_friends', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    openidlist = []
    if jdata['ret'] == 0:
        openidlist = [fid['openid'] for fid in jdata['items']]

    jdata = api.call('/v3/user/get_multi_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenids': '_'.join(openidlist)
    })
    pretty_show(jdata)

    jdata = api.call('/v3/user/is_setup', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    jdata = api.call('/v3/relation/is_friend', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenid': '0000000000000000000000000326E4AA'
    })
    pretty_show(jdata)


def t_core_test():
    pf = 'tapp'
    jdata = api.call('/v3/user/get_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    jdata = api.call('/v3/relation/get_app_friends', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    pretty_show(jdata)

    openidlist = []
    if jdata['ret'] == 0:
        openidlist = [fid['openid'] for fid in jdata['items']]

    jdata = api.call('/v3/user/get_multi_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenids': '_'.join(openidlist)
    })
    pretty_show(jdata)


def t_other_test():
    pf = 'tapp'

    # jdata = api.call('/v3/relation/add_idol', {
    # 'pf': pf,
    # 'openid': openid,
    # 'openkey': openkey,
    # 'fopenids': '00000000000000000000000001223930',
    # })
    # pretty_show(jdata)

    jdata = api.call('/v3/user/get_other_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenid': openid,
    })
    pretty_show(jdata)


def qqshow_test():
    pf = 'qzone'

    jdata = api.call('/v3/qqshow/get_app_friends', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'cmd': 0
    })
    pretty_show(jdata)


def iedstar_test():
    pf = 'qzone'

    jdata = api.call('/v3/user/is_area_login', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
    })
    pretty_show(jdata)


def unity_test():
    pf = 'qzone'

    jdata = api.call('/v3/user/set_achivement', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'user_attr': json.dumps(dict(level=10), ensure_ascii=False),
    })
    pretty_show(jdata)

    jdata = api.call('/v3/user/get_achivement', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenids': '0000000000000000000000000326E4AA_0000000000000000000000000039811C',
    })
    pretty_show(jdata)
    return

    jdata = api.call('/v3/user/friends_vip_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenids': '0000000000000000000000000326E4AA_0000000000000000000000000039811C',
    })
    pretty_show(jdata)

    jdata = api.call('/v3/user/is_vip', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
    })
    pretty_show(jdata)

    jdata = api.call('/v3/user/is_login', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
    })
    pretty_show(jdata)

    jdata = api.call('/v3/spread/verify_invkey', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'iopenid': '0000000000000000000000000039811C',
        'itime': '1334202931',
        'invkey': '8A96E97D5F393241F04CFD0255550241'
    })
    pretty_show(jdata)


def csec_test():
    pf = 'qzone'

    jdata = api.call('/v3/csec/word_filter', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'content': '唉' * 1000,
    })
    pretty_show(jdata)

    jdata = api.call('/v3/csec/is_forbidden', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
    })
    pretty_show(jdata)


def music_test():
    pf = 'qzone'

    jdata = api.call('/v3/music/get_song_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
    })
    pretty_show(jdata)


def main():
    # qz_core_test()
    # qp_core_test()
    # py_core_test()
    # kx_core_test()
    # manyou_core_test()
    # xingcloud_core_test()
    # t_core_test()
    # t_other_test()
    # qqshow_test()
    # iedstar_test()
    # unity_test()
    # csec_test()
    music_test()


if __name__ == '__main__':
    for it in range(0, 1000):
        if it == 1:
            break
        main()
