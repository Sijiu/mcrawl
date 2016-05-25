# -*- coding: utf-8 -*-



DH_UNIT = [
    {'en': u'Piece', 'code': u'00000000000000000000000000000003', 'zh': u'\u4ef6'},
    {'en': u'Dozen', 'code': u'00000000000000000000000000000001', 'zh': u'\u6253'},
    {'en': u'Feet', 'code': u'00000000000000000000000000000002', 'zh': u'\u82f1\u5c3a'},
    {'en': u'Set', 'code': u'00000000000000000000000000000004', 'zh': u'\u5957'},
    {'en': u'Gram', 'code': u'00000000000000000000000000000005', 'zh': u'\u514b'},
    {'en': u'Inch', 'code': u'00000000000000000000000000000008', 'zh': u'\u82f1\u5bf8'},
    {'en': u'Kilogram', 'code': u'00000000000000000000000000000009', 'zh': u'\u5343\u514b'},
    {'en': u'Kilometre', 'code': u'00000000000000000000000000000010', 'zh': u'\u5343\u7c73'},
    {'en': u'Liter', 'code': u'00000000000000000000000000000011', 'zh': u'\u5347'},
    {'en': u'Metric Tonne', 'code': u'00000000000000000000000000000012', 'zh': u'\u5428'},
    {'en': u'Meter', 'code': u'00000000000000000000000000000013', 'zh': u'\u7c73'},
    {'en': u'Milliliter', 'code': u'00000000000000000000000000000015', 'zh': u'\u6beb\u5347'},
    {'en': u'Ounce', 'code': u'00000000000000000000000000000016', 'zh': u'\u76ce\u53f8'},
    {'en': u'Pair', 'code': u'00000000000000000000000000000017', 'zh': u'\u53cc'},
    {'en': u'Pound', 'code': u'00000000000000000000000000000018', 'zh': u'\u78c5'},
    {'en': u'Square Yard', 'code': u'00000000000000000000000000000022', 'zh': u'\u5e73\u65b9\u7801'},
    {'en': u'Square Meter', 'code': u'00000000000000000000000000000023', 'zh': u'\u5e73\u65b9\u7c73'},
    {'en': u'Square Feet', 'code': u'00000000000000000000000000000024', 'zh': u'\u5e73\u65b9\u82f1\u5c3a'},
    {'en': u'Yard', 'code': u'00000000000000000000000000000028', 'zh': u'\u7801'},
    {'en': u'Centimeter', 'code': u'00000000000000000000000000000029', 'zh': u'\u5398\u7c73'},
    {'en': u'Carton', 'code': u'00000000000000000000000000000033', 'zh': u'\u7bb1'}
]


def find_by_code(code):
    for unit in DH_UNIT:
        if code == unit["code"]:
            return unit
    return DH_UNIT[0]


def find_by_en_name(en_name):
    for unit in DH_UNIT:
        if en_name == unit["en"]:
            return unit
    return DH_UNIT[0]


def find_by_zh_name(zh_name):
    for unit in DH_UNIT:
        if zh_name == unit["en"]:
            return unit
    return DH_UNIT[0]


def get_dh_units():
    return DH_UNIT