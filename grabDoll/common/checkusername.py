# -*- coding: utf-8 -*-
__author__ = 'maxijie'
import re

def check_user_name(s):
    p3=re.compile("^0\d{2,3}[\d\+]{7,13}$|^1[34578][\d\+]{9,12}$|^147\d{8}|[^\._-][\w\.+-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+")
    email_or_mobile = p3.match(s)
    if email_or_mobile:
        return True
    else:
        return False
