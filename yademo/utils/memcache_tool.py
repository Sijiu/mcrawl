#coding=utf8
__author__ = 'changdongsheng'


import traceback
from functools import wraps
import memcache
from furion.config import setting
from furion.lib.utils.logger_util import logger


memcache_machine = setting.get("memcache_machine")

memcache_client = memcache.Client(memcache_machine, debug=0)


def traceback_wrap(func):
    @wraps(func)
    def new_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            logger.warning(traceback.format_exc())
    return new_func


@traceback_wrap
def memcache_delete(key, **kwargs):
    ret = memcache_client.delete(str(key), **kwargs)
    return ret


@traceback_wrap
def memcache_delete_multi(keys, **kwargs):
    keys = [str(key) for key in keys]
    ret = memcache_client.delete_multi(keys, **kwargs)
    return ret


@traceback_wrap
def memcache_get(key, **kwargs):
    return memcache_client.get(str(key), **kwargs)


@traceback_wrap
def memcache_set(key, val, **kwargs):
    key = str(key)
    if 'time' not in kwargs:
        kwargs['time'] = 3600*24*7
    return memcache_client.set(key, val, **kwargs)


@traceback_wrap
def memcache_get_multi(keys, **kwargs):
    return memcache_client.get_multi(keys, **kwargs)


@traceback_wrap
def memcache_set_multi(mapping, **kwargs):
    return memcache_client.set_multi(mapping, **kwargs)


@traceback_wrap
def memcache_incr(key):
    return memcache_client.incr(key)


@traceback_wrap
def memcache_decr(key):
    return memcache_client.decr(key)


def join_cache_key(*keys):
    return '#'.join([str(key) for key in keys])