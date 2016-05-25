# -*- coding:utf-8 -*-
__author__ = 'xuhe'


StatusCode = {
    "Draft": "4",
    "UploadSuccess": "1",
    "UploadFailed": "-1",
    "WaitingUpload": "3",
    "TransFailed": "-2",
    "Translating": "2",
    "ImageFailed": "0",
    "Uploading": "1000",
    "Online": "10000",
    "Offline": "10001",
    "Auditing": "10002",
    "Rejected": "10003",
    "Sold": "10005",
    "Unsold": "10006",
    "BothLine": "20000",
    "Editing": "20001",
    "EditFailed": "20002",
}

OnlineStatus = [
    StatusCode["Online"], StatusCode["Offline"], StatusCode["Auditing"],
    StatusCode["Rejected"], StatusCode["Sold"], StatusCode["Unsold"],
    StatusCode["BothLine"], StatusCode["Editing"], StatusCode["EditFailed"]
]

StatusDesc = {
    "1": {
        "text": u"上传成功",
        "style": "#5cb85c"
    },
    "-1": {
        "text": u"上传失败",
        "style": "#d9534f"
    },
    "3": {
        "text": u"等待上传",
        "style": "#5bc0de"
    },
    "-2": {
        "text": u"翻译失败",
        "style": "#d9534f"
    },
    "2": {
        "text": u"翻译中",
        "style": "#5bc0de"
    },
    "0": {
        "text": u"图片处理失败",
        "style": "#f0ad4e"
    },
    "4": {
        "text": u"草稿",
        "style": ""
    },
    "1000": {
        "text": u"上传中",
        "style": "#f0ad4e"
    },
    "10000": {
        "text": u"在售商品",
        "style": ""
    },
    "10001": {
        "text": u"下架商品",
        "style": ""
    },
    "10002": {
        "text": u"审核中",
        "style": ""
    },
    "10003": {
        "text": u"审核不通过",
        "style": ""
    }

}

LockingStatus = [
    "1", "2", "1000", "10000"
]

UnLockingStatus = [
    "-1", "0", "3", "-2"
]

ResultStatus = {
    "upload_price": "更新价格",
    "upload_stock": "更新库存",
    "offline": "下架",
    "upload_base": "更新基本信息"
}

OrderStatus = {
    "WaitingProcess": "100",
    "WaitingDelivery": "200",
    "VirtualDelivery": "300",
    "HadDelivery": "400",
    "Finish": "500",
    "Error": "999",
}
OrderTag = {
    "100": "买家未付款",
    "200": "未填写报关信息",
    "300": "未分配物流方式",
    "400": "未分配运单号",
    "500": "未打印",
}


