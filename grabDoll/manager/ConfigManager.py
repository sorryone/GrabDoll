# -*- coding: utf-8 -*-
from pyexcel_xls import get_data
from grabDoll.models.config_model import ConfigModel
from django.conf import settings

__author__ = 'du_du'

config_path = r'../config/'
file_name = 'machine.xlsx'


def read_xls_file(path, name):
    xls_data = get_data(path+name)
    config_data = dict()
    for sheet_n in xls_data.keys():
        sheet_data = xls_data[sheet_n]
        for i, val in enumerate(sheet_data, 0):
            if i == 0:
                continue
            elif i == 1:
                config_keys = val
            else:
                row_data = dict()
                for index, value in enumerate(val):
                    row_data[config_keys[index]] = value
                config_data[val[0]] = row_data
    add_redis(config_data, name.split('.')[0])


def add_redis(data, name):
    model = ConfigModel(name)
    model.set_values(data)


def test():
    config_group = ('egg', 'item', 'artifact', 'doll', 'machine', 'shop', 'doll_upgrade', 'pve', 'turntable', 'task', 'user_lv ', 'box')
    data = dict()
    for config_name in config_group:
        data[config_name] = ConfigModel(config_name).get_model_info()
    print(data)


def read_files():
    config_dir = settings.CONFIG_DIR
    read_xls_file(config_dir, 'egg.xlsx')
    read_xls_file(config_dir, 'item.xlsx')
    read_xls_file(config_dir, 'artifact.xlsx')
    read_xls_file(config_dir, 'doll.xlsx')
    read_xls_file(config_dir, 'machine.xlsx')
    read_xls_file(config_dir, 'shop.xlsx')
    read_xls_file(config_dir, 'doll_upgrade.xlsx')
    read_xls_file(config_dir, 'pve.xlsx')
    read_xls_file(config_dir, 'turntable.xlsx')
    read_xls_file(config_dir, 'task.xlsx')
    read_xls_file(config_dir, 'user_lv.xlsx')
    read_xls_file(config_dir, 'box.xlsx')
    print test()


if __name__ == '__main__':
    print test()

