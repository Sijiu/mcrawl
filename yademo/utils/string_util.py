#coding=utf8
__author__ = 'changdongsheng'


import hashlib


class StringUtil(object):
    @classmethod
    def str2md5(cls, strings):
        md5 = hashlib.md5()
        md5.update(strings)
        return md5.hexdigest()