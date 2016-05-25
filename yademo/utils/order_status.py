#coding=utf8
__author__ = 'Administrator'

ALI_ORDER_STATUS = {
    'PLACE_ORDER_SUCCESS': '等待买家付款',
    'IN_CANCEL': '买家申请取消',
    'WAIT_SELLER_SEND_GOODS': '等待发货',
    'SELLER_PART_SEND_GOODS': '部分发货',
    'WAIT_BUYER_ACCEPT_GOODS': '等待买家收货',
    'FUND_PROCESSING': '等待放款',
    'FINISH': '结束订单',
    'IN_ISSUE': '纠纷订单',
    'IN_FROZEN': '冻结订单',
    'WAIT_SELLER_EXAMINE_MONEY': '等待确认金额',
    'RISK_CONTROL': '风控订单',
    '等待买家付款': 'PLACE_ORDER_SUCCESS',
    '买家申请取消': 'IN_CANCEL',
    '等待发货': 'WAIT_SELLER_SEND_GOODS',
    '等待买家收货': 'WAIT_BUYER_ACCEPT_GOODS',
    '等待放款': 'FUND_PROCESSING',
    '结束订单': 'FINISH',
    '纠纷订单': 'IN_ISSUE',
    '风控订单':  'RISK_CONTROL',
    '等待确认金额': 'WAIT_SELLER_EXAMINE_MONEY',
    '部分发货': 'SELLER_PART_SEND_GOODS',
    '冻结订单': 'IN_FROZEN'
}

EBAY_ORDER_STATUS = {
    'Active': '活动',
    'All': '全部',
    'CancelPending': '取消处理中',
    'Completed': '完成',
    'Shipped': '已发货',
    '活动': 'Active',
    '全部': 'All',
    '取消处理中': 'CancelPending',
    '完成': 'Completed',
    '已发货': 'Shipped'
}

PLATFORM = {
    'eBay': 'ebay',
    'AliExpress': 'ali',
    'Amazon': 'amazon'
}


