# -*- coding: utf-8 -*-
from lib.redis_model import StringModel, HashModel
__author__ = 'du_du'


class HandBookModel(HashModel):
    def get_model_info(self):
        return self.get_all()

    # 增加经验
    def add_book_exp(self, book_id, num=1):
        res = self.get_book_info_by_id(book_id)
        if res is not False:
            cur_exp = res.get('exp', 0)
            res['exp'] = cur_exp + num
            self.set_value(res)
        return False

    # 获得当前图鉴的经验
    def get_book_exp(self, book_id):
        res = self.get_book_info_by_id(book_id)
        if res is not False:
            return res.get('exp', 0)
        return 0

    # 获得当前图鉴的是否解锁
    def get_book_lock(self, book_id):
        # 50001 不需要解锁
        if book_id == 50001:
            return True
        res = self.get_book_info_by_id(book_id)
        if res is not False:
            return res.get('unlock', False)
        return False

    # 解锁图鉴
    def unlock_book(self, book_id):
        res = self.set_value(book_id, {'unlock': False})
        return res

    # 获取当前图鉴的信息
    def get_book_info_by_id(self, book_id):
        res = self.get_value(book_id, False)
        if res:
            return eval(res)
        return False

