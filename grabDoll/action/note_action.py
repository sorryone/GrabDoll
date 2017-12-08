# -*- coding: utf-8 -*-
from grabDoll.models.note_model import NoteModel


class NoteAction:
    def __init__(self, u_id):
        self.u_id = u_id
        self.cache = NoteModel(u_id)

    def count_record(self, key_name, time=0, func=None):
        # exists = $this->cache->exists(key_name);
        exists = False
        if exists:
            # this->cache->incr(key_name);
            pass
        if time != 0:
            # $this->cache->setTimeout($key, timerMaker()+$time);
            pass
        else:
            if func is not None:
                pass
            # this->cache->set($key, 1, 0, timerMaker()+$time);
        return True

