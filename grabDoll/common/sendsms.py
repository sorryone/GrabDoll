# -*- coding: utf-8 -*-
__author__ = 'maxijie'

import requests
import json
from django.conf import settings
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkcore.client import AcsClient
from django.core.mail import send_mail
import uuid

acs_client = AcsClient(settings.ACCESS_KEY_ID, settings.ACCESS_KEY_SECRET,\
                       settings.REGION)


def send_sms(phone_numbers, template_param=None):
    smsRequest = SendSmsRequest.SendSmsRequest()
    # 申请的短信模板编码,必填
    smsRequest.set_TemplateCode(settings.ALIYUNSNSTEMPCODE)

    # 短信模板变量参数
    if template_param is not None:
        smsRequest.set_TemplateParam(json.dumps(template_param))

    # 设置业务请求流水号，必填。
    business_id = uuid.uuid1()
    smsRequest.set_OutId(business_id)

    # 短信签名
    smsRequest.set_SignName(settings.SIGNNAME);

    # 短信发送的号码列表，必填。
    smsRequest.set_PhoneNumbers(phone_numbers)

    # 调用短信发送接口，返回json
    smsResponse = acs_client.do_action_with_exception(smsRequest)
    if not smsResponse:
        return False

    data = eval(smsResponse)
    print("sendsms data = ", data)
    if data["Code"] != "OK":
        return False

    return True

"""
def sendsmsfunction(mobile, content):
    try:
        data_dict = dict()
        index = mobile.find("+")
        if index > 0:
            mobile = mobile[:index]

        data_dict['mobile'] = str(mobile).strip()
        data_dict['message'] = content+"【顺顺教育】"
        #if settings.DATABASES['default']['HOST'] != 'liuyuxiao.mysql.rds.aliyuncs.com':
        #    data_dict['mobile'] = '15001185171'
        #    print u'[DEV mode] send sms to test mobile({}):'.format(
        #        data_dict['mobile']), data_dict['message']

        resp = requests.post(settings.SMS_URL,auth=("api",
                            settings.SMS_KEY),data=data_dict,timeout=5, verify=False)
        result = json.loads(resp.content)

        if result[u'msg'] == u'ok':
            print "send sms success, mobile=%s" % mobile
            return True
        else:
            print result[u'msg']
            return False

    except Exception, e:
        print e.message
        return False


def sendsmsfunction2(mobile, template_code, **params):
    ###### 测服发给开发人员
    if settings.DATABASES['default']['HOST'] != 'liuyuxiao.mysql.rds.aliyuncs.com':
        mobile = '13466557647'
    ###### 测服发给开发人员
    index = mobile.find("+", 10)
    if index > 10:
        mobile = mobile[:index]

    dayu = Alidayu(**settings.ALIDAYU_PARAMS)
    dayu.setopt(Alidayu.SMS_FREE_SIGN_NAME, u"顺顺留学")    # 短信签名
    dayu.setopt(Alidayu.SMS_TEMPLATE_CODE, template_code)   # 模版代码
    dayu.setopt(Alidayu.SMS_PARAMS, params)                 # 模版参数
    dayu.setopt(Alidayu.REC_NUMS, [mobile])                 # 接收手机号
    success = dayu.send()

    if not success:
        print dayu.error.errorcode, dayu.error.message, dayu.error.subcode
        print dayu.error.submsg

    return success
"""

def sendemailfunction(email_list, content, title):
    try:
        result = send_mail(title, content, settings.EMAIL_HOST_USER, email_list)
        if result == 1:
            return True
        else:
            return False

    except Exception, e:
        print e.message
        return False
