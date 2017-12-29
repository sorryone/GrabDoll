# -*- coding: utf-8 -*-
from pyexcel_xls import get_data
from grabDoll.models.config_model import ConfigModel
from django.conf import settings
import json

__author__ = 'du_du'


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
    # model.set_values(data)
    with open(name + '.json', 'w') as json_file:
        json_file.write(json.dumps(data))
    print(data)


def read_files():
    config_dir = settings.CONFIG_DIR
    read_xls_file(config_dir, 'egg.xlsx') 
