
# -*- coding: utf-8 -*-

# @author: xuhe
# @date: 15/5/5
# @description: 


import redis
from furion.config import settings


redis_type = ["LIST", "DICT", "SET"]
pool = redis.ConnectionPool(host=settings.redis_host,
                            port=settings.redis_port,
                            db=settings.redis_db,
                            max_connections=50)
conn = redis.Redis(connection_pool=pool, socket_timeout=60, charset='utf-8', errors='strict')


class RedisUtil(object):
    RU_L = "list"
    RU_S = "set"
    RU_D = "dict"

    def __init__(self, collection=None, r_type=None):
        if r_type and r_type.upper() not in redis_type:
            raise Exception
        self.collection = collection
        self.r_type = r_type

    def set(self, key, value=None):
        if self.r_type == "list":
            return conn.rpush(self.collection, key)
        elif self.r_type == "set":
            return conn.sadd(self.collection, key)
        elif self.r_type == "dict":
            return conn.hset(self.collection, key, value)
        else:
            return conn.set(key, value)

    def get(self, key=None):
        if self.r_type == "list":
            return conn.lpop(self.collection)
        elif self.r_type == "set":
            return conn.smembers(self.collection)
        elif self.r_type == "dict":
            return conn.hget(self.collection, key)
        else:
            return conn.get(key)

    def get_set(self, key):
        value = self.get(key)
        conn.hset(self.collection, key, value)
        return value

    def drop_member(self, key):
        if self.r_type == "set":
            return conn.srem(self.collection, key)
        elif self.r_type == "dict":
            return conn.hdel(self.collection, key)
        else:
            raise Exception

    @classmethod
    def find_key(cls, pattern):
        return conn.keys(pattern)

    @classmethod
    def drop_key(cls, key):
        if cls.find_key(key):
            return conn.delete(key)

    def set_expiration(self, name, expiration):
        if self.r_type:
            raise Exception
        return conn.expire(name, expiration)

    def is_member(self, value):
        if self.r_type == "set":
            return conn.sismember(self.collection, value)
        elif self.r_type == "list":
            return value in conn.lrange(self.collection, 0, -1)
        else:
            raise Exception

    def get_members(self):
        if self.r_type == "list":
            return conn.lrange(self.collection, 0, -1)
        elif self.r_type == "set":
            return conn.smembers(self.collection)
        else:
            raise Exception

    def increase(self, key):
        if self.r_type:
            raise Exception
        return str(conn.incr(key, 1))

    def decrease(self, key):
        if self.r_type:
            raise Exception
        return str(conn.decr(key, 1))

    def next(self):
        return conn.rpoplpush(self.collection, self.collection)

    @property
    def length(self):
        if self.r_type == "list":
            return conn.llen(self.collection)
        elif self.r_type == "set":
            return conn.scard(self.collection)
        elif self.r_type == "dict":
            return conn.hlen(self.collection)
        else:
            raise Exception
