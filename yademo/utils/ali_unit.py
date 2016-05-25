# -*- coding: utf-8 -*-


ALI_UNIT = [
    {'code': u'100000000', 'en': u'bag', 'zh': u'\u888b'},
    {'code': u'100000001', 'en': u'barrel', 'zh': u'\u6876'},
    {'code': u'100000002', 'en': u'bushel', 'zh': u'\u84b2\u5f0f\u8033'},
    {'code': u'100078580', 'en': u'carton', 'zh': u'\u7bb1'},
    {'code': u'100078581', 'en': u'centimeter', 'zh': u'\u5398\u7c73'},
    {'code': u'100000003', 'en': u'cubic meter', 'zh': u'\u7acb\u65b9\u7c73'},
    {'code': u'100000004', 'en': u'dozen', 'zh': u'\u6253'},
    {'code': u'100078584', 'en': u'feet', 'zh': u'\u82f1\u5c3a'},
    {'code': u'100000005', 'en': u'gallon', 'zh': u'\u52a0\u4ed1'},
    {'code': u'100000006', 'en': u'gram', 'zh': u'\u514b'},
    {'code': u'100078587', 'en': u'inch', 'zh': u'\u82f1\u5bf8'},
    {'code': u'100000007', 'en': u'kilogram', 'zh': u'\u5343\u514b'},
    {'code': u'100078589', 'en': u'kiloliter', 'zh': u'\u5343\u5347'},
    {'code': u'100000008', 'en': u'kilometer', 'zh': u'\u5343\u7c73'},
    {'code': u'100078559', 'en': u'liter', 'zh': u'\u5347'},
    {'code': u'100000009', 'en': u'long ton', 'zh': u'\u82f1\u5428'},
    {'code': u'100000010', 'en': u'meter', 'zh': u'\u7c73'},
    {'code': u'100000011', 'en': u'metric ton', 'zh': u'\u516c\u5428'},
    {'code': u'100078560', 'en': u'milligram', 'zh': u'\u6beb\u514b'},
    {'code': u'100078596', 'en': u'milliliter', 'zh': u'\u6beb\u5347'},
    {'code': u'100078597', 'en': u'millimeter', 'zh': u'\u6beb\u7c73'},
    {'code': u'100000012', 'en': u'ounce', 'zh': u'\u76ce\u53f8'},
    {'code': u'100000014', 'en': u'pack', 'zh': u'\u5305'},
    {'code': u'100000013', 'en': u'pair', 'zh': u'\u53cc'},
    {'code': u'100000015', 'en': u'piece', 'zh': u'\u4ef6/\u4e2a'},
    {'code': u'100000016', 'en': u'pound', 'zh': u'\u78c5'},
    {'code': u'100078603', 'en': u'quart', 'zh': u'\u5938\u8131'},
    {'code': u'100000017', 'en': u'set', 'zh': u'\u5957'},
    {'code': u'100000018', 'en': u'short ton', 'zh': u'\u7f8e\u5428'},
    {'code': u'100078606', 'en': u'square feet', 'zh': u'\u5e73\u65b9\u82f1\u5c3a'},
    {'code': u'100078607', 'en': u'square inch', 'zh': u'\u5e73\u65b9\u82f1\u5bf8'},
    {'code': u'100000019', 'en': u'square meter', 'zh': u'\u5e73\u65b9\u7c73'},
    {'code': u'100078609', 'en': u'square yard', 'zh': u'\u5e73\u65b9\u7801'},
    {'code': u'100000020', 'en': u'ton', 'zh': u'\u5428'},
    {'code': u'100078558', 'en': u'yard', 'zh': u'\u7801'}
]


def find_by_code(code):
    for unit in ALI_UNIT:
        if code == unit["code"]:
            return unit


def find_by_en_name(en_name):
    for unit in ALI_UNIT:
        if en_name == unit["en"]:
            return unit
    return ALI_UNIT[24]


def find_by_zh_name(zh_name):
    for unit in ALI_UNIT:
        if zh_name == unit["en"]:
            return unit
    return ALI_UNIT[24]


def get_ali_units():
    return ALI_UNIT