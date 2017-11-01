from grabDoll.models.base_model import BaseModel
from grabDoll.models.friend_model import FriendModel, FriendTable, FriendTableSerializer
__author__ = 'du_du'


class FriendAction(BaseModel):

    def __init__(self, u_id):
        self.u_id = u_id
        super(FriendAction, self).__init__(
                    u_id, FriendModel, FriendTable, FriendTableSerializer, True)

    # 移除当前娃娃机里的娃娃蛋
    def get_model_info(self):
        data = self.get_all()
        res = dict()
        for key, value in data.items():
            res[key] = eval(value)
        return res
