# -*- coding: utf-8 -*-
from grabDoll.models.machine_model import MachineModel
from grabDoll.models.note_model import NoteModel
from grabDoll.models.user import User as UserModel
import grabDoll.logics.book_logic as book_logic
import time
import random
__author__ = 'du_du'


def get_machine_info(uid):
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


# 根据时间自动刷新娃娃蛋
def refresh_model_info(uid):
    note_model = NoteModel(uid)
    cur_time = time.time()
    # 获取当前的机器号
    mach_id = note_model.get_cur_machine()
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
    eggs = [10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008]
    rand_x = [5, 6, 7, 8, 9]
    rand_y = [20, 21, 22, 23, 24, 25]
    for index in range(20):
        data[str(mach_id) + '_' + str(index)] = {'id': random.choice(eggs), 'x': random.choice(rand_x), 'y': random.choice(rand_y), 'r': 30}
    res = mach.add_egg_list(data)
    return res


# print switch_machine('ED57884CAA078DF9E0E08750D98CA834', 50002)
