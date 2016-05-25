# -*- coding: utf-8 -*-

# @author: xuhe
# @date: 15/12/17
# @description: 


import requests
import traceback
import ujson as json
from config import settings
from yademo.utils.logger_util import logger


class HttpSQL(object):

    host = "https://www.actneed.com/data/"

    @classmethod
    def req(cls, path, retry=0, **data):
        req_url = cls.host + path
        for key in data:
            value = data[key]
            if isinstance(value, dict):
                data[key] = json.dumps(value)
        data["api_key"] = settings.api_key
        logger.info(u"HttpSQL正在请求的URL是%s" % req_url)
        logger.info(data["api_key"])
        logger.info(data)
        try:
            res = requests.post(req_url, data=data, timeout=20)
            logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            logger.info(res.request)
            logger.info(u"HttpSQL从ActNeed获取到的数据结果是%s" % res.text)
            result = res.json()
            if not result["success"]:
                logger.info("#" * 40)
                logger.warning(result["message"])
                logger.info("#" * 40)
                raise Exception
            return json.loads(result["data"])
        except Exception, e:
            logger.warning(traceback.format_exc(e))
            if retry >= 3:
                raise Exception
            return cls.req(path, retry + 1, **data)