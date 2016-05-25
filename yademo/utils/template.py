# -*- coding: utf-8 -*-


from copy import deepcopy

UniversalTemplate = {
    "Title": "",
    "SecondTitle": "",
    "Description": "",
    "ShortDescription": "",
    "Brand": "",
    "UPC": "",
    "Manufacture": "",
    "TaxClass": "",
    "ShipmentType": "",
    "ProductType": "",
    "VariationTheme": "",
    "Condition": {
        "ID": "",
        "Name": ""
    },
    "VideoURL": "",
    "PictureURLs": [],
    "SizeType": "",
    "KeyWords": ["", "", "", "", ""],
    "BulletPoints": ["", "", "", "", ""],
    "Quantity": "",
    "StartPrice": "",
    "ReservePrice": "",
    "BuyItNowPrice": "",
    "ListingType": "FixedPriceItem",
    "ListingDuration": "",
    "PrivateListing": True,
    "DispatchTimeMax": "",
    "ItemType": "",
    "SpecialValue": "",
    "ParentSKU": "",
    "CategoryRoot": "",
    "IsAdult": False,
    "Department": "",
    "CollectGroup": 0,
    "Category": {
        "ID": "",
        "Name": "",
    },
    "SecondCategory": {
        "ID": "",
        "Name": "",
    },
    "Group": {
        "ID": 0,
        "Name": "",
    },
    "SecondGroup": {
        "ID": 0,
        "Name": "",
    },
    "CategoryUID": 0,
    "PackageType": False,
    "LotNum": 1,
    "BulkSell": False,
    "BrandSeller": "0",
    "ProductIdType": "",
    "ProductUnit": "",
    "PackageLength": "",
    "PackageWidth": "",
    "PackageHeight": "",
    "PackageWeight": "",
    "PackageContent": "",
    "ShippingWeight": "",
    "LengthUnit": "",
    "WeightUnit": "",
    "GrossWeight": "",
    "SelfDefineWeight": False,
    "FreightTemplateID": "",
    "SizeChartTemplateID": "",
    "PromiseTemplateID": "",
    "ReduceStrategy": "",
    "ProductSpecifics": [],
    "ProductSKUs": [],
    "SourceInfo": {
        "Platform": "",
        "Site": "",
        "SiteID": "",
        "ProductID": "",
        "Link": "",
    },
    "MSRP": "",
    "LandingURL": "",
    "ShippingCost": 0,
    "ShippingTime": "",
    "Status": "",
    "IsTemplate": True,
    "Sale": {
        "SalePrice": "",
        "SaleDateFrom": "",
        "SaleDateTo": ""
    }
}
product_sku = {
    "Stock": "",
    "Price": "",
    "VariationSpecifics": "",
    "SKU": "",
    "SkuID": "",
    "ShippingCost": "",
    "ShippingTime": "",
    "StandardID": {
        "Type": "",
        "Value": "",
    }
}
product_sku_specifics = {
    "Image": "",
    "Name": "",
    "NameID": "",
    "Value": "",
    "ValueID": "",
}
product_specifics = {
    "Name": "",
    "Value": "",
    "NameID": "",
    "ValueID": ""
}
self_define_weight = {
    "BaseUnit": "",
    "AddUnit": "",
    "AddWeight": ""
}
bulk_sell = {
    "BulkOrder": "",
    "BulkDiscount": ""
}
amazon_product_sku_specifics = {
    "Color": "",
    "Size": "",
    "Image": "",
    "ColorMap": "",
    "SizeMap": ""
}


def generate_template():
    return deepcopy(UniversalTemplate)
