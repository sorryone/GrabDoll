# -*- coding: utf-8 -*-
__author__ = 'liuyuxiao'

import datetime
import time

class Mytime():

    def transferTimestampToDatetime(self,timestamp):
        timestamp = int(timestamp)/1000
        out_time = datetime.datetime.fromtimestamp(timestamp)
        return out_time

    def transferDatetimeToStr(self,datetime):
        return datetime.strftime('%Y-%m-%d+%H:%M:%S')

    def trandferTimeStampToHumanRead(self,timestamp):
        timestamp = int(timestamp)/1000
        return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    def transferStringToDatetime(self,timestr):
        date_object = datetime.datetime.strptime(timestr,'%Y-%m-%d+%H:%M:%S')+datetime.timedelta(hours=8)
        return date_object

    def transferDateStringToDatetime(self,timestr):
        date_object = datetime.datetime.strptime(timestr,'%Y-%m-%d')+datetime.timedelta(hours=8)
        return date_object

    def transfer_datetime_to_timestamp(self, dtime):
        return time.mktime(dtime.timetuple())


    def trandferTimeStampToDate(self,timestamp):
        timestamp = int(timestamp)/1000
        return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

    @classmethod
    def timelist_to_time(cls, dict_obj, key):
        """
            in = {'create_at' : ["1444983850000", "1444989850000"]}
            return = {'create_at_start' : 1444983850000, "create_at_end": 1444989850000}
        """
        s_time = time.strftime("%Y-%m-%d %H:%M:%S" ,time.localtime(int(dict_obj[key][0]) / 1000 ))
        e_time = time.strftime("%Y-%m-%d %H:%M:%S" ,time.localtime(int(dict_obj[key][1]) / 1000 ))
        dict_obj[key + '_start'] = datetime.datetime.strptime(s_time, "%Y-%m-%d %H:%M:%S")
        dict_obj[key + '_end'] = datetime.datetime.strptime(e_time, "%Y-%m-%d %H:%M:%S")
        dict_obj.pop(key)
