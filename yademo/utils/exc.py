#coding=utf8
__author__ = 'changdongsheng'


class FBaseException(Exception):
    msg = "furion base exception"


class AccountAuthorizedException(FBaseException):
    msg = "furion account authorized exception"


class AccountException(FBaseException):
    msg = "account money error"


class NullArgumentException(Exception):
    msg = "some arguments is null"


class MissArgumentError(Exception):
    msg = "some required arguments not supported"


class NullFeedException(Exception):
    msg = "the feed is null"


class NullRecordException(Exception):
    msg = "the translate record is null"


class GroupUnionError(Exception):
    msg = "union is error"


class FeedTemplateImportError(Exception):
    msg = "the feed has been import to the public template"


class FeedTemplateExportError(Exception):
    msg = "the feed must be import to public before export"


class AliExpress401Error(Exception):
    msg = "request 401"


class ImageSpaceNoCapacity(Exception):
    msg = "image space is less than 10M"


class AccessDenyError(Exception):
    msg = "you have no right to access the shop"


class AuthExpireError(Exception):
    msg = "the authority of shop has expired"


class TaskNeedRetry(Exception):
    msg = "the error need to be retry"


class CheckFeedRetryError(Exception):
    msg = "the feed is not finished, try again"


class TimeoutException(Exception):
    msg = "furion time out exception"
