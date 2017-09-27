# -*- coding: utf-8 -*-
from grabDoll.models.machine_model import MachineModel
from grabDoll.models.note_model import NoteModel
from grabDoll.models.user import User as UserModel
from grabDoll.models.doll_model import DollModel
from grabDoll.models.item_model import ItemModel
from grabDoll.models.gacha_model import GachaModel
from grabDoll.models.handbook_model import HandBookModel
import grabDoll.logics.book_logic as book_logic
import time
import random
__author__ = 'du_du'


def get_machine_info(uid):
    refresh_model_info(uid)
    mach_model = MachineModel(uid)
    return mach_model.get_model_info()


def get_note_info(uid):
    note_model = NoteModel(uid)
    return note_model.get_model_info()


def switch_machine(uid, machine_id):
    note_model = NoteModel(uid)
    # 需要判定 machine_id 是否可以切换  防止信息诈骗
    if book_logic.check_book_unlock(uid, machine_id):
        return note_model.set_cur_machine(machine_id)
    return False


def grab_egg(uid, key_id):
    mach_model = MachineModel(uid)
    egg = mach_model.get_egg_info(key_id)
    if egg is False:
        return False
    item_id = egg.get('id', False)
    if item_id is not False:
        del_res = mach_model.delete_egg(key_id)
    else:
        return False
    # 存在的话删除掉
    if del_res:
        # 奖励
        awards = get_award(item_id)
        item_model = ItemModel(uid)
        doll_model = DollModel(uid)
        gacha_model = GachaModel(uid)
        book_model = HandBookModel(uid)
        user = UserModel(uid)
        res = dict()
        for a_id, ct in awards.iteritems():
            # 如果是金币添加金币
            if a_id == "gold":
                user.add_gold(ct)
                res[a_id] = ct
            # 如果是钻石添加钻石
            elif a_id == "diamond":
                user.add_diamond(ct)
                res[a_id] = ct
            # 经验
            elif a_id == "exp":
                user.add_gold(ct)
                res[a_id] = ct
            # 如果是道具添加道具
            elif int(a_id)/10000 == 2:
                item_model.add_model(a_id, ct)
            elif int(a_id)/10000 == 3:
                gacha_model.add_model(a_id, ct)
            elif int(a_id)/10000 == 4:
                res['doll'] = doll_model.add_model(a_id)
            else:
                pass
        # 图鉴加经验
        note_model = NoteModel(uid)
        res['book_exp'] = book_model.add_book_exp(note_model.get_cur_machine(), 1)
        return res
    print("item  is not exits")
    return False


# 查看奖励
def get_award(item_id):
    ct = 1000
    data = dict()
    data['gold'] = ct
    doll_id = random.randint(40001, 40008)
    data[doll_id] = 1
    print('get_award', data)
    return data


# 根据时间自动刷新娃娃蛋
def refresh_model_info(uid):
    note_model = NoteModel(uid)
    cur_time = time.time()
    # 获取当前的机器号
    mach_id = note_model.get_cur_machine()
    # 如果没有记录 是个新手的话 设置默认的机器
    if mach_id is None:
        mach_id = 50001
        note_model.set_cur_machine(mach_id)
    egg_refresh_time = note_model.get_machine_create_time(mach_id)
    cd = 300
    if egg_refresh_time is None or cur_time > egg_refresh_time + cd:
        note_model.set_machine_create_time(mach_id)
        reset_machine_egg_info(uid, mach_id)


# 重置娃娃机里的娃娃蛋
def reset_machine_egg_info(uid, mach_id):
    mach = MachineModel(uid)
    # mach.delete() 旧数据删除大可不必  只要数量相同就会被覆盖
    data = dict()
    eggs = [10001, 10002, 10003, 10004]
    rand_x = [5, 6, 7, 8, 9]
    rand_y = [20, 21, 22, 23, 24, 25]
    for index in range(20):
        data[str(mach_id) + '_' + str(index)] = {'id': random.choice(eggs), 'x': random.choice(rand_x), 'y': random.choice(rand_y), 'r': 30}
    res = mach.add_egg_list(data)
    return res


# print switch_machine('ED57884CAA078DF9E0E08750D98CA834', 50002)
# print grab_egg('ED57884CAA078DF9E0E08750D98CA834', '50001_18')
