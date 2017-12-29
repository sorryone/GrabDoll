# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
__author__ = 'maxijie'


urlpatterns = patterns("",
                       url(r'^test/', 'grabDoll.views.test.test'),
                       url(r'^get_user/', 'grabDoll.views.user.get_user'),
                       url(r'^get_user_data/', 'grabDoll.views.user.get_user_data'),
                       url(r'^start_grab/', 'grabDoll.views.game_method.start_grab'),
                       url(r'^grab_egg/', 'grabDoll.views.game_method.grab_egg'),
                       # 解锁
                       url(r'^hatch_unlock/', 'grabDoll.views.game_method.hatch_unlock'),
                       # 加速孵化
                       url(r'^hatch_speed/', 'grabDoll.views.game_method.hatch_speed'),
                       url(r'^hatch_open/', 'grabDoll.views.game_method.hatch_open'),
                       url(r'^hatch_discard/', 'grabDoll.views.game_method.hatch_discard'),
                       url(r'^open_egg_by_cost/', 'grabDoll.views.game_method.open_egg_by_cost'),
                       # 切换娃娃机
                       url(r'^switch_machine/', 'grabDoll.views.game_method.switch_machine'),
                       # 刷新重置娃娃机
                       url(r'^reset_machine/', 'grabDoll.views.game_method.reset_machine'),
                       # Debug定位游戏代码的位置
                       url(r'^get_debug/', 'grabDoll.views.game_method.get_debug'),
                       # 测试用户的平台信息
                       url(r'^get_info/', 'grabDoll.views.game_test.get_info'),
                       # 获取好友信息
                       url(r'^get_my_friend_info/', 'grabDoll.views.friend_method.get_my_friend_info'),
                       # 进入好友家
                       url(r'^enter_friend_home/', 'grabDoll.views.friend_method.enter_friend_home'),
                       # 申请成为好友
                       url(r'^add_friend/', 'grabDoll.views.friend_method.add_friend'),
                       # 接受好友请求
                       url(r'^accept_friend/', 'grabDoll.views.friend_method.accept_friend'),
                       # 拒绝好友请求
                       url(r'^refuse_friend/', 'grabDoll.views.friend_method.refuse_friend'),
                       # 移除好友
                       url(r'^remove_friend/', 'grabDoll.views.friend_method.remove_friend'),
                       # 抢劫好友金币
                       url(r'^rob_money/', 'grabDoll.views.friend_method.rob_money'),
                       # 抢劫好友娃娃
                       url(r'^rob_doll/', 'grabDoll.views.friend_method.rob_doll'),
                       url(r'^buy_shop/', 'grabDoll.views.game_method.buy_shop'),
                       url(r'^use_item/', 'grabDoll.views.game_method.use_item'),
                       url(r'^set_fight/', 'grabDoll.views.fight_method.set_fight'),
                       url(r'^set_explore/', 'grabDoll.views.fight_method.set_explore'),
                       url(r'^fight_against/', 'grabDoll.views.fight_method.fight_against'),
                       url(r'^catch/', 'grabDoll.views.fight_method.catch'),
                       url(r'^refresh_income_info/', 'grabDoll.views.island_method.refresh_income_info'),
                       url(r'^award_income/', 'grabDoll.views.island_method.award_income'),
                       url(r'^upgrade_artifact/', 'grabDoll.views.game_method.upgrade_artifact'),
                       url(r'^buy_vit/', 'grabDoll.views.game_method.buy_vit'),
                       url(r'^get_pve_info/', 'grabDoll.views.pve_method.get_pve_info'),
                       url(r'^open_pve/', 'grabDoll.views.pve_method.open_pve'),
                       url(r'^refresh_pve_info/', 'grabDoll.views.pve_method.refresh_pve_info'),
                       url(r'^get_pve_award/', 'grabDoll.views.pve_method.get_pve_award'),
                       url(r'^get_mail_award/', 'grabDoll.views.mail_method.get_mail_award'),
                       url(r'^delete_all_mail/', 'grabDoll.views.mail_method.delete_all_mail'),
                       url(r'^get_all_mail_award/', 'grabDoll.views.mail_method.get_all_mail_award'),
                       url(r'^try_once/', 'grabDoll.views.turntable_method.try_once'),
                       url(r'^try_five_times/', 'grabDoll.views.turntable_method.try_five_times'),
                       )
