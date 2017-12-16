# -*- coding: utf-8 -*-
from grabDoll.action.machine_action import MachineAction
from grabDoll.models.note_model import NoteModel
from grabDoll.action.user_action import UserAction
from grabDoll.action.hero_action import HeroAction
from grabDoll.action.item_action import ItemAction
from grabDoll.action.hatch_action import HatchAction
from grabDoll.action.book_action import HandBookAction
from grabDoll.models.config_model import ConfigModel
import grabDoll.logics.book_logic as book_logic
import time
import random
__author__ = 'du_du'


def get_machine_info(uid):
    refresh_model_info(uid)
    mach_model = MachineAction(uid)
    return mach_model.get_model_info()


def get_note_info(uid):
    note_model = NoteModel(uid)
    return note_model.get_model_info()


def get_book_info(uid):
    action = HandBookAction(uid)
    return action.get_model_info()


def switch_machine(uid, machine_id):
    note_model = NoteModel(uid)
    # 需要判定 machine_id 是否可以切换  防止信息诈骗
    if book_logic.check_book_unlock(uid, machine_id):
        return note_model.set_cur_machine(machine_id)
    return False


def reset_machine(uid, mach_id):
    note_model = NoteModel(uid)
    cur_time = time.time()
    egg_refresh_time = note_model.get_machine_create_time(mach_id)
    cd = 600
    # 剩余时间
    remain_time = cur_time - egg_refresh_time - cd
    cost_gold = 100
    user_action = UserAction(uid)
    cur_gold = user_action.get_gold()
    if cur_gold < cost_gold:
        return False
    check_cost = user_action.reduce_gold(cost_gold)
    # 需要先扣钱
    if check_cost:
        note_model.set_machine_create_time(mach_id)
        res = {
            'eggs': reset_machine_egg_info(uid, mach_id),
            'costType': 'gold',
            'costValue': cost_gold,
            'mach_id': mach_id,
            'cur_time': cur_time,
        }
        return res
    return False


def start_grab(uid, key_id):
    user_action = UserAction(uid)
    vit = user_action.get_vit()
    vit_cost = 1
    if vit < vit_cost or user_action.reduce_vit(vit_cost) is False:
        return False
    config = ConfigModel('egg').get_config_by_id(key_id)
    probability = int(config['lv']) / 100
    rand = random.random()
    res = dict()
    res['res'] = True if rand <= probability else False
    note_model = NoteModel(uid)
    note_model.set_value(key_id, res['res'])
    return res


def grab_egg(uid, key_id, eggs):
    mach_action = MachineAction(uid)
    egg = mach_action.get_egg_info(key_id)
    eggs = eggs.encode('utf-8')
    eggs = eval(eggs)
    if egg is False:
        print("egg  is not exits")
        return False
    item_id = egg.get('id', False)
    if item_id is False:
        return False
    config = ConfigModel('egg').get_config_by_id(item_id)
    if config['lv'] <= 2:
        res = open_egg(uid, item_id)
    else:
        hatch_action = HatchAction(uid)
        available_hatch = hatch_action.get_hatch_available()
        if available_hatch is None:
            return False
        elif mach_action.delete_egg(key_id):
            res = {'hatch': hatch_action.add_model_index(item_id, available_hatch['pos'])}
        else:
            return False
    # 更新保存蛋的位置
    note_model = NoteModel(uid)
    mach_id = note_model.get_cur_machine()
    cur_eggs_keys = mach_action.get_egg_group(mach_id)
    values = {k: v for k, v in eggs.items() if k in cur_eggs_keys and k != key_id}
    mach_action.add_egg_list(values)
    return res


def save_eggs_pos_info():
    pass


def open_egg(uid, egg_id):
    # 奖励
    awards = get_award(egg_id)
    item_action = ItemAction(uid)
    hero_action = HeroAction(uid)
    book_action = HandBookAction(uid)
    user_action = UserAction(uid)
    res = dict()
    for a_id, ct in awards.iteritems():
        # 如果是金币添加金币
        if a_id == "gold":
            user_action.add_gold(ct)
            res[a_id] = ct
        # 如果是钻石添加钻石
        elif a_id == "diamond":
            user_action.add_diamond(ct)
            res[a_id] = ct
        # 经验
        elif a_id == "exp":
            user_action.add_gold(ct)
            res[a_id] = ct
        # 如果是道具添加道具
        elif int(a_id) / 10000 == 2:
            item_action.add_model(a_id, ct)
        elif int(a_id) / 10000 == 4:
            if hero_action.get_doll_exist(a_id) is False:
                res['doll'] = hero_action.add_model(a_id)
            else:
                cur_hero = hero_action.get_doll_info_by_id(a_id)
                hero_config_model = ConfigModel('doll_upgrade')
                cur_lv_config = hero_config_model.get_config_by_id(70000 + cur_hero['lv'])
                max_exp = cur_lv_config['exp']
                max_lv = 5
                add_exp = 1
                # 新的经验值
                exp = cur_hero['exp'] + add_exp
                if exp >= max_exp:
                    if cur_hero['lv'] < max_lv:
                        cur_hero['lv'] += 1
                        cur_hero['exp'] = exp - max_exp
                        hero_action.set_value(a_id, cur_hero)
                        res['hero_lv_up'] = True
                    else:
                        res['hero_lv_up'] = False
                        # 满级了
                        if cur_hero['exp'] < max_exp:
                            cur_hero['exp'] = max_exp
                            hero_action.set_value(a_id, cur_hero)
                        else:
                            # 经验槽也满了已经
                            add_exp = 0
                else:
                    cur_hero['exp'] = exp
                    hero_action.set_value(a_id, cur_hero)
                    res['hero_lv_up'] = False
                # 如果已经有这个英雄了 就发金币吧
                # user_action.add_gold(10)
                # res['gold'] = 10
                cur_hero['add_exp'] = add_exp
                res['doll'] = cur_hero
                res['hero_exist'] = a_id
        else:
            pass
    # 图鉴加经验
    note_model = NoteModel(uid)
    res['book_exp'] = book_action.add_book_exp(note_model.get_cur_machine(), 1)
    unlock_next_book = book_logic.refresh_lock(uid, note_model.get_cur_machine())
    if unlock_next_book:
        res['egg'] = reset_machine_egg_info(uid, unlock_next_book)
    return res
    pass


# 查看奖励
def get_award(item_id):
    data = dict()
    data['gold'] = random.randrange(10, 50)
    doll_id = random.randint(40001, 40150)
    data[doll_id] = 1
    check_award = data.popitem()
    print check_award[0]
    print check_award[1]
    return check_award


# 根据时间自动刷新娃娃蛋
def refresh_model_info(uid):
    note_model = NoteModel(uid)
    mach_model = MachineAction(uid)
    cur_time = time.time()
    # 获取当前的机器号
    mach_id = note_model.get_cur_machine()
    # 如果没有记录 是个新手的话 设置默认的机器
    if mach_id is None:
        mach_id = 50001
        note_model.set_cur_machine(mach_id)
    my_egg_group = mach_model.get_egg_group(mach_id)
    if my_egg_group.__len__() > 0:
        return
    egg_refresh_time = note_model.get_machine_create_time(mach_id)
    cd = 600
    if egg_refresh_time is None or cur_time > egg_refresh_time + cd:
        note_model.set_machine_create_time(mach_id)
        return reset_machine_egg_info(uid, mach_id)


# 重置娃娃机里的娃娃蛋
def reset_machine_egg_info(uid, mach_id):
    config_model = ConfigModel('machine')
    mach_config = config_model.get_config_by_id(mach_id)
    egg_group = mach_config['eggGroup']
    egg_list = eval(egg_group)
    random_list = []
    for key, value in egg_list.items():
        random_list.extend([key] * value)
    slice_list = random.sample(random_list, 20)
    mach = MachineAction(uid)
    data = dict()
    rand_x = [5, 6, 7, 8, 9]
    rand_y = [20, 21, 22, 23, 24, 25]
    for index in range(len(slice_list)):
        data[str(mach_id) + '_' + str(index)] = {'id': slice_list[index], 'x': random.choice(rand_x), 'y': random.choice(rand_y), 'r': 30}
    res = mach.add_egg_list(data)
    if res:
        return data
    return False


if __name__ == "__main__":
    print switch_machine('ED57884CAA078DF9E0E08750D98CA834', 50001)
    # print grab_egg('ED57884CAA078DF9E0E08750D98CA834', '50001_3')
    # print refresh_model_info('ED57884CAA078DF9E0E08750D98CA834')
