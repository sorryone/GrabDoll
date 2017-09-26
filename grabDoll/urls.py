# -*- coding: utf-8 -*-
__author__ = 'maxijie'
from django.conf.urls import patterns, include, url

urlpatterns = patterns("",
    url(r'^test', 'grabDoll.views.test.test'),
    url(r'^get_user', 'grabDoll.views.user.get_user'),
    url(r'^set_user', 'grabDoll.views.user.set_user'),
    url(r'^grab_egg', 'grabDoll.views.game_method.grab_egg'),
    url(r'^speed_up', 'grabDoll.views.game_method.speed_up'),     # 加速孵化
    url(r'^switch_machine', 'grabDoll.views.game_method.switch_machine'),     # 测试用
    url(r'^get_debug', 'grabDoll.views.game_method.get_debug'),     # Debug定位游戏代码的位置
    url(r'^get_info', 'grabDoll.views.game_test.get_info'),  # 测试用户的平台信息
)
