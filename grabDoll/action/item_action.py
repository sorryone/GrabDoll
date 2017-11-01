from grabDoll.models.base_model import BaseModel
from grabDoll.models.item_model import ItemModel, ItemTable, ItemTableSerializer


class ItemAction(BaseModel):
    def __init__(self, u_id):
        self.u_id = u_id
        super(ItemAction, self).__init__(
                    u_id, ItemModel, ItemTable, ItemTableSerializer, True)

    def get_model_info(self):
        return self.get_all()

    # 增加物品
    def add_model(self, item_id, num=1):
        res = self.incr(item_id, num)
        if res is not False:
            return True
        return False

    # 移除物品
    def remove_model(self, item_id, num=1):
        cur_ct = self.get_value(item_id)
        if cur_ct < num:
            return False
        res = self.incr(item_id, -num)
        if res == 0 or res is not False:
            return True
