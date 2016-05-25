#coding=utf8


AMAZON_AUTH = {
    "US": "https://developer.amazonservices.com",
    "Canada": "https://developer.amazonservices.ca",
    "Germany": "https://developer.amazonservices.de",
    "Spain": "https://developer.amazonservices.es",
    "France": "https://developer.amazonservices.fr",
    "India": "https://developer.amazonservices.in",
    "Italy": "https://developer.amazonservices.it",
    "UK": "https://developer.amazonservices.co.uk",
    "Japan": "https://developer.amazonservices.jp",
    "China": "https://developer.amazonservices.com.cn"
}

AMAZON_MWS = {
    "CA": {
        "end_point": "https://mws.amazonservices.ca",
        "market_id": "A2EUQ1WTGCTBG2"
    },
    "US": {
        "end_point": "https://mws.amazonservices.com",
        "market_id": "ATVPDKIKX0DER"
    },
    "DE": {
        "end_point": "https://mws-eu.amazonservices.com",
        "market_id": "A1PA6795UKMFR9"
    },
    "ES": {
        "end_point": "https://mws-eu.amazonservices.com",
        "market_id": "A1RKKUPIHCS9HS"
    },
    "FR": {
        "end_point": "https://mws-eu.amazonservices.com",
        "market_id": "A13V1IB3VIYZZH"
    },
    "IN": {
        "end_point": "https://mws.amazonservices.in",
        "market_id": "A21TJRUUN4KGV"
    },
    "IT": {
        "end_point": "https://mws-eu.amazonservices.com",
        "market_id": "APJ6JRA9NG5V4"
    },
    "UK": {
        "end_point": "https://mws-eu.amazonservices.com",
        "market_id": "A1F83G8C2ARO7P"
    },
    "JP": {
        "end_point": "https://mws.amazonservices.jp",
        "market_id": "A1VC38T7YXB528"
    },
    "CN": {
        "end_point": "https://mws.amazonservices.com.cn",
        "market_id": "AAHKV2X7AFYLW"
    }
}

FEED_TYPES = {
    #FEED TYPE
    'offer':                  '_POST_OFFER_ONLY_DATA_',                             # Offer
    'order_acknowledgement':  '_POST_ORDER_ACKNOWLEDGEMENT_DATA_',                  # Order
    'order_cancellation':     '_POST_FULFILLMENT_ORDER_CANCELLATION_REQUEST_DATA_', # Order
    'order_fulfillment':      '_POST_ORDER_FULFILLMENT_DATA_',                      # Order
    'product_data':           '_POST_PRODUCT_DATA_',                                # Product
    'product_image':          '_POST_PRODUCT_IMAGE_DATA_',                          # Product
    'product_inventory':      '_POST_INVENTORY_AVAILABILITY_DATA_',                 # Product
    'product_item':           '_POST_ITEM_DATA_',                                   # Product
    'product_override':       '_POST_PRODUCT_OVERRIDES_DATA_',                      # Product
    'product_pricing':        '_POST_PRODUCT_PRICING_DATA_',                        # Product
    'product_relationship':   '_POST_PRODUCT_RELATIONSHIP_DATA_',                   # Product
    'shipping_override':      '_POST_SHIPPING_OVERRIDE_DATA_',                      # Shipping
    'webstore_item':          '_POST_WEBSTORE_ITEM_DATA_',                          # Webstore
    # Flat-File Feeds
    'flat_book':              '_POST_FLAT_FILE_BOOKLOADER_DATA_',                   # Book
    'flat_book_uiee':         '_POST_UIEE_BOOKLOADER_DATA_',                        # Book: Universal Information Exchange Environment
    'flat_product_converge':  '_POST_FLAT_FILE_CONVERGENCE_LISTINGS_DATA_',         # Product: Merging
    'flat_product_data':      '_POST_FLAT_FILE_LISTINGS_DATA_',                     # Product
    'flat_product_inventory': '_POST_FLAT_FILE_INVLOADER_DATA_',                    # Product
    'flat_product_price_inv': '_POST_FLAT_FILE_PRICEANDQUANTITYONLY_UPDATE_DATA_',  # Product
}


#: Feed Methods. Maps FEED_TYPES to data-types
FEED_METHODS = {
    'offer':                  'xml',
    'order_acknowledgement':  'xml',
    'order_cancellation':     'xml',
    'order_fulfillment':      'xml',
    'product_data':           'xml',
    'product_image':          'xml',
    'product_inventory':      'xml',
    'product_item':           'xml',
    'product_override':       'xml',
    'product_pricing':        'xml',
    'product_relationship':   'xml',
    'shipping_override':      'xml',
    'webstore_item':          'xml',
    'flat_book':              'flat-file',
    'flat_book_uiee':         'flat-file',
    'flat_product_converge':  'flat-file',
    'flat_product_data':      'flat-file',
    'flat_product_inventory': 'flat-file',
    'flat_product_price_inv': 'flat-file',
}

#: Content types. Key is ENDPOINT aliased name. Maps FEED_TYPE, FEED_METHOD and ENTPOINT to content-type.
CONTENT_TYPES = {
    'ca': {
        'xml': 'text/xml',
        'flat-file': 'text/tab-separated-values; charset=iso-8859-1',
    },
    'cn': {
        'xml': 'text/xml',
        'flat-file': 'text/tab-separated-values; charset=UTF-8',
        'flat-file-alt': 'text/tab-separated-values; charset=UTF-16',
    },
    'eu': {
        'xml': 'text/xml',
        'flat-file': 'text/tab-separated-values; charset=iso-8859-1',
    },
    'in': {
        'xml': 'text/xml',
        'flat-file': 'text/tab-separated-values; charset=iso-8859-1',
    },
    'jp': {
        'xml': 'text/xml',
        'flat-file': 'text/tab-separated-values; charset=Shift_JIS',
    },
    'us': {
        'xml': 'text/xml',
        'flat-file': 'text/tab-separated-values; charset=iso-8859-1',
    },
}

#: Processing statuses..
PROCESSING_STATUSES = {
    'cancelled': '_CANCELLED_',
    'done': '_DONE_',
    'in_progress': '_IN_PROGRESS_',
    'submitted': '_SUBMITTED_'
}

API_LIMIT = {
    "SubmitFeed": {
        "MAX_COUNT": 15,
        "RESUME": 120
    },
    "GetFeedSubmissionList": {
        "MAX_COUNT": 10,
        "RESUME": 45
    },
    "GetFeedSubmissionResult": {
        "MAX_COUNT": 15,
        "RESUME": 60
    },
     "RequestReport": {
        "MAX_COUNT": 15,
        "RESUME": 60
    },
    "GetReportRequestList": {
        "MAX_COUNT": 10,
        "RESUME": 45
    },
    "GetReport": {
        "MAX_COUNT": 15,
        "RESUME": 60
    },
    "GetMatchingProduct": {
        "MAX_COUNT": 20,
        "RESUME": 0.5
    },
    "GetLowestOfferListingsForSKU": {
        "MAX_COUNT": 20,
        "RESUME": 0.1
    },
    "GetMatchingProductForId": {
        "MAX_COUNT": 20,
        "RESUME": 0.5
    },
    "GetMyPriceForSKU": {
        "MAX_COUNT": 20,
        "RESUME": 0.1
    }
}

SPECIFICS = [
    "Color", "Size", "SizeMap", "ColorMap", "InnerMaterialType", "IsAdult", "MaterialComposition",
    "OuterMaterialType", "StyleName", "SeasonAndCollectionYear", "Department", "Material", "mfg_minimum",
    "TargetAudience", "MaterialType", "FrameMaterialType", "ItemShape", "LensColor", "LensColorMap",
    "LensMaterialType", "LensWidth", "LensWidthUnit", "MagnificationStrength", "PolarizationType", "MfrPartNumber",
    "HardDiskInterface", "HardDriveSize", "HardwarePlatform", "OperatingSystem", "RAMType", "ProcessorCount",
    "ProcessorSeries", "ProcessorSpeed", "ProcessorBrand", "RAMSize", "CupSize", "Inseam", "WaistSize", "ItemLength",
    "OccasionAndLifestyle", "BandSizeNumeric", "AdditionalFeatures", "MaxUnit", "MaximumExpandableSize",
    "LineSizeUnit", "LineSize", "PaperSize", "NumberOfItems", "mfg_maximum", "ManufacturerSafetyWarning", "UnitCount",
    "PaperSizeUnit", "InkColor", "NumberOfPieces", "BandColor", "Flavor", "PatternName", "Scent", "StyleKeywords",
    "ModelName",
    "ClothingType", "PitchCircleDiameter", "GemType", "MetalType", "RingSize", "Length", "LengthUnit",
    "TotalDiamondWeightUnit",
    "SizePerPearl", "TotalDiamondWeightUnit", "MetalStamp", "CapacityUnitMeasure", "UnitCountMeasure", "Capacity",
    "GolfLoftUnit",
    "ShaftLengthUnit", "WeightSupportedUnit", "GolfLoft", "GolfFlex", "GripSize", "GripType", "Hand", "ShaftLength",
    "ShaftMaterial", "Shape", "TensionLevel", "Style", "WeightSupported", "LengthUnitOfMeasure", "DisplayLength",
    "WidthUnitOfMeasure",
    "DisplayWidth", "ExteriorFinish", "Wattage", "Voltage", "CapType", "SpecificUses", "CustomerPackageType",
    "Indications", "ItemPackageQuantity", "SpeakerAmplificationType", "MusicalStyle", "ModelYear",
    "AdditionalSpecifications", "ESRBRating", "MediaFormat", "LeatherType", "CollectionName", "Season", "LegStyle"
]

VARIATION_SPECIFICS = ["Color", "Size", "Material", "PaperSize", "MaximumExpandableSize", "LineSize", "NumberOfItems",
    "BandColor", "Flavor", "PatternName", "Scent", "Length", "MetalType", "WeightSupported",
    "StyleName", "TotalDiamondWeight", "SizePerPearl", "RingSize", "Capacity", "UnitCount",
    "TensionLevel", "Style", "Hand", "ShaftMaterial", "GolfFlex", "GolfLoft", "LensColor",
    "GripSize",
    "HeadSize", "GripType", "ShaftLength", "Shape", "CupSize", "DisplayWidth", "DisplayLength",
    "CustomerPackageType"
]

