# -*- coding: utf-8 -*-
from grabDoll.models.base_model import BaseModel
from grabDoll.models.item_model import ItemModel, ItemTable, ItemTableSerializer


class NoteAction:
    def __init__(self, u_id):
        self.u_id = u_id

