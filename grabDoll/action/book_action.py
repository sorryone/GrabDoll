from grabDoll.models.base_model import BaseModel
from grabDoll.models.handbook_model import HandBookModel, HandBookTable, HandBookTableSerializer
__author__ = 'du_du'


class HandBookAction(BaseModel):

    def __init__(self, u_id):
        self.u_id = u_id
        super(HandBookAction, self).__init__(
                    u_id, HandBookModel, HandBookTable, HandBookTableSerializer, True)

    def get_model_info(self):
        return self.get_all()

    # 增加经验
    def add_book_exp(self, book_id, num=1):
        res = self.get_book_info_by_id(book_id)
        if res is not False:
            cur_exp = res.get('exp', 0)
        else:
            res = dict()
            cur_exp = 0
        res['exp'] = cur_exp + num
        return self.set_value(book_id, res)

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
        return self.has_key(book_id)

    # 解锁图鉴
    def unlock_book(self, book_id):
        res = self.set_value(book_id, {'exp': 0})
        if res == 0 or res is not False:
            return True
        return res

    # 获取当前图鉴的信息
    def get_book_info_by_id(self, book_id):
        res = self.get_value(book_id, False)
        if res:
            return eval(res)
        return False