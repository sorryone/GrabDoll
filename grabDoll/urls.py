# -*- coding: utf-8 -*-
__author__ = 'maxijie'
from django.conf.urls import patterns, include, url

urlpatterns = patterns("",
    url(r'^test', 'grabDoll.views.test.test'),
    url(r'^get_user', 'grabDoll.views.user.get_user'),
    url(r'^set_user', 'grabDoll.views.user.set_user'),
    url(r'^grab_egg', 'grabDoll.views.game_method.grab_egg'),
    url(r'^speed_up', 'grabDoll.views.game_method.speed_up'),     # 加速孵化
    url(r'^create_user', 'grabDoll.views.game_method.create_user'),     # 测试用
)
