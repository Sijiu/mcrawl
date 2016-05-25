# -*- coding=utf-8 -*-

"""
@author:lance
@date:
@version:
@description:
"""
from lib.nosql.redis_util import RedisUtil
from yademo.utils.logger_util import logger


currency = {
    "USD": "美元",
    "CAD": "加元",
    "GBP": "英镑",
    "EUR": "欧元",
    "AUD": "澳元",
    "INR": "印度卢比",
    "HKD": "港元",
    "SGD": "新加坡元",
    "MYR": "马来西亚林吉特",
    "PHP": "菲律宾比索",
    "PLN": "波兰兹罗提",
    "CHF": "瑞士法郎",
    "JPY": "日元",
    "CNY": "人民币元",
}


def transform(src_currency, tar_currency, src_value):
    currency_key = "%s:%s" % (src_currency, tar_currency)
    rate = float(RedisUtil().get(currency_key))
    return str(round(rate * float(src_value) / 100, 2))


def get_rate(src_currency, tar_currency):
    currency_key = "%s:%s" % (src_currency, tar_currency)
    return float(RedisUtil().get(currency_key))
