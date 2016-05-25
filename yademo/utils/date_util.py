#! -*- coding:utf-8 -*-


import sys
import time
from datetime import datetime, timedelta
reload(sys)
sys.setdefaultencoding('utf-8')


class DateUtil(object):
    """
    提供系统所需日期时间等相关静态数据

    """

    @classmethod
    def get_end_date(cls, start_date, alive_days):
        """获取过期日期"""
        start_date_arr = str(start_date).split('-')
        start_date = datetime(int(start_date_arr[0]), int(start_date_arr[1]), int(start_date_arr[2]))
        alive_days = timedelta(days=alive_days)
        end_date = start_date + alive_days
        return end_date.strftime('%Y-%m-%d')

    @classmethod
    def get_sys_date(cls):
        """系统当前日期"""
        local_time = time.localtime()
        sys_date = time.strftime('%Y-%m-%d', local_time)
        return sys_date

    @classmethod
    def str_2_date(cls, data_str, split_str):
        """将字符串转换成datetime类型"""
        str_arr = data_str.split(split_str)
        if len(str_arr) < 3:
            return None
        format_date = datetime(int(str_arr[0]), int(str_arr[1]), int(str_arr[2]))
        return format_date

    @classmethod
    def str_2_time(cls, date_str, format_str):
        return datetime.strptime(date_str, format_str)

    @classmethod
    def get_sys_time(cls, format_str=None):
        """系统当前时间"""
        sys_time = datetime.now()
        if format_str:
            return sys_time.strftime(format_str)
        return sys_time

    @classmethod
    def timedelta_to_time(cls, time_delta):
        """将time_delta装换成日，时，分，秒"""
        days = time_delta.days
        hours = time_delta.seconds / 3600
        minutes = (time_delta.seconds - hours * 3600) / 60
        seconds = time_delta.seconds % 60
        return days, hours, minutes, seconds

    @classmethod
    def get_date_distance(cls, pre_time_str, post_time_str):
        """计算两个时间字符串的时间差，返回timedelta"""
        pre_time = cls.str_2_time(pre_time_str, "%Y-%m-%d %H:%M:%S")
        post_time = cls.str_2_time(post_time_str, "%Y-%m-%d %H:%M:%S")
        return (post_time - pre_time).seconds

    @classmethod
    def time_to_datetime(cls, timestamp):
        """将timestamp转换为datetime类型"""
        return datetime.fromtimestamp(timestamp)

