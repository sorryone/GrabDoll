# -*- coding: utf-8 -*-
__author__ = 'maxijie'

import json
from django.http import HttpResponse
# from django.http import HttpRequest


def test(request):
    print("this is test")
    return HttpResponse(json.dumps({"result": "this is test11"}),
                        content_type='application/json')
