#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from openapi_v3 import OpenAPIV3

# 正式的
appid = 1106233605
appkey = 'STwl4MAK67bcemOd'
# 我自己的测试服务器
# appid = 1106423014
# appkey = 'PSqsIO5GwAu4wUL4'


iplist = ('api.urlshare.cn',)
# iplist = ('172.27.0.91',)
# iplist = ('10.6.207.119:9191',)
# iplist = ('10.166.146.171',)
# iplist = ('10.166.146.174',)
# iplist = ('172.25.36.57:8191',)
# iplist = ('proxy.qq.com',)


# openid = '000000000000000000000000199B6A55'
# openkey = '84BAEDACC5B512FED2FA653695624491'

openid = '000000000000000000000000199B6A55'
openkey = '84BAEDACC5B512FED2FA653695624491'
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






def main():
    qz_core_test()


if __name__ == '__main__':
    main()
