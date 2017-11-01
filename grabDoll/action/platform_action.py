# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.platform_model import PlatformModel, PlatformTable, PlatformTableSerializer
__author__ = 'du_du'


class PlatformAction(BaseModel):

    def __init__(self, u_id):
        self.u_id = u_id
        super(PlatformAction, self).__init__(
                    u_id, PlatformModel, PlatformTable, PlatformTableSerializer, True)

    def get_model_info(self):
        data = self.get_all()
        return data