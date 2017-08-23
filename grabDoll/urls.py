# -*- coding: utf-8 -*-
__author__ = 'maxijie'
from django.conf.urls import patterns, include, url

urlpatterns = patterns("",
    url(r'^test', 'grabDoll.views.test.test'),
    url(r'^get_user', 'grabDoll.views.user.get_user'),
    url(r'^set_user', 'grabDoll.views.user.set_user'),
    url(r'^get_inventory', 'grabDoll.views.inventory.get_inventory'),
)
