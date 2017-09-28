# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
__author__ = 'maxijie'


urlpatterns = patterns("",
                       url(r'^test', 'grabDoll.views.test.test'),
                       url(r'^get_user', 'grabDoll.views.user.get_user'),
                       url(r'^set_user', 'grabDoll.views.user.set_user'),
                       url(r'^grab_egg', 'grabDoll.views.game_method.grab_egg'),
                       # 加速孵化
                       url(r'^speed_up', 'grabDoll.views.game_method.speed_up'),
                       # 切换娃娃机
                       url(r'^switch_machine', 'grabDoll.views.game_method.switch_machine'),
                       # Debug定位游戏代码的位置
                       url(r'^get_debug', 'grabDoll.views.game_method.get_debug'),
                       # 测试用户的平台信息
                       url(r'^get_info', 'grabDoll.views.game_test.get_info'),
                       # 获取好友信息
                       url(r'^get_my_friend_info', 'grabDoll.views.game_method.get_my_friend_info'),
                       # 进入好友家
                       url(r'^enter_friend_home', 'grabDoll.views.game_method.enter_friend_home'),
                       # 申请成为好友
                       url(r'^add_friend', 'grabDoll.views.game_method.add_friend'),
                       # 接受好友请求
                       url(r'^accept_friend', 'grabDoll.views.game_method.accept_friend'),
                       # 拒绝好友请求
                       url(r'^refuse_friend', 'grabDoll.views.game_method.refuse_friend'),
                       # 移除好友
                       url(r'^remove_friend', 'grabDoll.views.game_method.remove_friend'),
                       )
