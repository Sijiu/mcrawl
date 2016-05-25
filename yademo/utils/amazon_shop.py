# -*- coding=utf-8 -*-


SHOP_CRAWL = {
    "http://www.amazon.com": {
        "headers": {
            "Accept":"*/*",
            "Accept-Encoding":"gzip, deflate",
            "Connection":"keep-alive",
            "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
            "Cookie":"""x-wl-uid=1dSc8ngaJcA+zESw+d3IaeSb8R6d+CEeTrpBTPKSbqK34Oy5RC4H/opx0sDF3VoXTFxSBOXRdovpQd8Z3gbug6E0owmznSEutnNKBMG0l6bQLRrYbXH0SqxB/epQMZxAd+1SZ++OVa+Y=; amznacsleftnav-434072922=1; lc-acbuk=en_US; x-acbuk="1WD?9Szl17NLYjr2rd38nhEe27f8vQP0P81CRTk6U8mPlyTt5Bc6w@Kn8NwWO0jZ"; s_vnum=1872999156664%26vn%3D3; s_nr=1443610582599-Repeat; s_dslv=1443610582600; lc-main=en_US; s_pers=%20s_dl%3D1%7C1444297711927%3B%20gpv_page%3DUS%253ASC%253A%2520SellerCentralLogin%7C1444297711931%3B%20s_ev15%3D%255B%255B%2527Typed/Bookmarked%2527%252C%25271441850750752%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271441850752439%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442234450573%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442234451487%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442480662774%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442480739067%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442804418296%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442804418997%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271443523953442%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271444295909519%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271444295911933%2527%255D%255D%7C1602148711933%3B; session-token=SMJ/zLivbCWU5gLKztXgsYOY3/UWQ+909LJlbwq1tAenRNO9zjS6YEJIxeb0+qLxJPOC1W+W3B/WNkU0e1zem3zVqaYk7xuGjwaj5Sk5kVlVGQivbMHXmra5b2T1nnCuykLy01nMTswiDZRTl4ycfEaKZaGZYJ/hq8xNHXGOvLnTdb5ivBU5c6bXtj3b3dBkEH7rF8S7s1A45b/Hh7qX0S8ZKftxkeijIMcHj3OfYMy2y2Ij532JqWPaUAlxD2ybG9fmtQHJJ8BeCZCd1+OJRKr/Ia04yidX; x-main="KCvGpS6JBZlAFUSl@0EQU7UYYdzBsPDbccPh14AVANCEoej2Q1yoh@qkuBfb4Wi1"; s_sess=%20c_m%3DundefinedTyped/BookmarkedTyped/Bookmarked%3B%20s_cc%3Dtrue%3B%20s_sq%3Damznsrvsprod%252Camznsrvsmainprod%253D%252526pid%25253DUS%2525253ASC%2525253A%25252520SellerCentralLogin%252526pidt%25253D1%252526oid%25253D%252525A0%252525A0Sign%25252520in%252525A0%252525A0%2525250A%252526oidt%25253D3%252526ot%25253DSUBMIT%3B; skin=noskin; ubid-main=178-2834543-3947633; session-id-time=2082787201l; session-id=177-4413589-2799362; csm-hit=1NA2Q8GBR6KY4Y0DRT74+s-0DPXK2MT9GHVFV143098|1444301549284""",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest"
        },
        "url": "http://www.amazon.com/gp/aag/ajax/searchResultsJson.html"
    },
    "http://www.amazon.ca": {
        "headers": {
            "Accept":"*/*",
            "Accept-Encoding":"gzip, deflate",
            "Connection":"keep-alive",
            "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
            "Cookie":"""x-wl-uid=1dSc8ngaJcA+zESw+d3IaeSb8R6d+CEeTrpBTPKSbqK34Oy5RC4H/opx0sDF3VoXTFxSBOXRdovpQd8Z3gbug6E0owmznSEutnNKBMG0l6bQLRrYbXH0SqxB/epQMZxAd+1SZ++OVa+Y=; amznacsleftnav-434072922=1; lc-acbuk=en_US; x-acbuk="1WD?9Szl17NLYjr2rd38nhEe27f8vQP0P81CRTk6U8mPlyTt5Bc6w@Kn8NwWO0jZ"; s_vnum=1872999156664%26vn%3D3; s_nr=1443610582599-Repeat; s_dslv=1443610582600; lc-main=en_US; s_pers=%20s_dl%3D1%7C1444297711927%3B%20gpv_page%3DUS%253ASC%253A%2520SellerCentralLogin%7C1444297711931%3B%20s_ev15%3D%255B%255B%2527Typed/Bookmarked%2527%252C%25271441850750752%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271441850752439%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442234450573%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442234451487%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442480662774%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442480739067%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442804418296%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442804418997%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271443523953442%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271444295909519%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271444295911933%2527%255D%255D%7C1602148711933%3B; session-token=SMJ/zLivbCWU5gLKztXgsYOY3/UWQ+909LJlbwq1tAenRNO9zjS6YEJIxeb0+qLxJPOC1W+W3B/WNkU0e1zem3zVqaYk7xuGjwaj5Sk5kVlVGQivbMHXmra5b2T1nnCuykLy01nMTswiDZRTl4ycfEaKZaGZYJ/hq8xNHXGOvLnTdb5ivBU5c6bXtj3b3dBkEH7rF8S7s1A45b/Hh7qX0S8ZKftxkeijIMcHj3OfYMy2y2Ij532JqWPaUAlxD2ybG9fmtQHJJ8BeCZCd1+OJRKr/Ia04yidX; x-main="KCvGpS6JBZlAFUSl@0EQU7UYYdzBsPDbccPh14AVANCEoej2Q1yoh@qkuBfb4Wi1"; s_sess=%20c_m%3DundefinedTyped/BookmarkedTyped/Bookmarked%3B%20s_cc%3Dtrue%3B%20s_sq%3Damznsrvsprod%252Camznsrvsmainprod%253D%252526pid%25253DUS%2525253ASC%2525253A%25252520SellerCentralLogin%252526pidt%25253D1%252526oid%25253D%252525A0%252525A0Sign%25252520in%252525A0%252525A0%2525250A%252526oidt%25253D3%252526ot%25253DSUBMIT%3B; skin=noskin; ubid-main=178-2834543-3947633; session-id-time=2082787201l; session-id=177-4413589-2799362; csm-hit=1NA2Q8GBR6KY4Y0DRT74+s-0DPXK2MT9GHVFV143098|1444301549284""",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest"
        },
        "url": "http://www.amazon.ca/gp/aag/ajax/searchResultsJson.html"
    },
    "http://www.amazon.co.uk": {
        "headers": {
            "Accept":"*/*",
            "Accept-Encoding":"gzip, deflate",
            "Connection":"keep-alive",
            "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
            "Cookie":"""x-wl-uid=1dSc8ngaJcA+zESw+d3IaeSb8R6d+CEeTrpBTPKSbqK34Oy5RC4H/opx0sDF3VoXTFxSBOXRdovpQd8Z3gbug6E0owmznSEutnNKBMG0l6bQLRrYbXH0SqxB/epQMZxAd+1SZ++OVa+Y=; amznacsleftnav-434072922=1; lc-acbuk=en_US; x-acbuk="1WD?9Szl17NLYjr2rd38nhEe27f8vQP0P81CRTk6U8mPlyTt5Bc6w@Kn8NwWO0jZ"; s_vnum=1872999156664%26vn%3D3; s_nr=1443610582599-Repeat; s_dslv=1443610582600; lc-main=en_US; s_pers=%20s_dl%3D1%7C1444297711927%3B%20gpv_page%3DUS%253ASC%253A%2520SellerCentralLogin%7C1444297711931%3B%20s_ev15%3D%255B%255B%2527Typed/Bookmarked%2527%252C%25271441850750752%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271441850752439%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442234450573%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442234451487%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442480662774%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442480739067%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442804418296%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271442804418997%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271443523953442%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271444295909519%2527%255D%252C%255B%2527Typed/Bookmarked%2527%252C%25271444295911933%2527%255D%255D%7C1602148711933%3B; session-token=SMJ/zLivbCWU5gLKztXgsYOY3/UWQ+909LJlbwq1tAenRNO9zjS6YEJIxeb0+qLxJPOC1W+W3B/WNkU0e1zem3zVqaYk7xuGjwaj5Sk5kVlVGQivbMHXmra5b2T1nnCuykLy01nMTswiDZRTl4ycfEaKZaGZYJ/hq8xNHXGOvLnTdb5ivBU5c6bXtj3b3dBkEH7rF8S7s1A45b/Hh7qX0S8ZKftxkeijIMcHj3OfYMy2y2Ij532JqWPaUAlxD2ybG9fmtQHJJ8BeCZCd1+OJRKr/Ia04yidX; x-main="KCvGpS6JBZlAFUSl@0EQU7UYYdzBsPDbccPh14AVANCEoej2Q1yoh@qkuBfb4Wi1"; s_sess=%20c_m%3DundefinedTyped/BookmarkedTyped/Bookmarked%3B%20s_cc%3Dtrue%3B%20s_sq%3Damznsrvsprod%252Camznsrvsmainprod%253D%252526pid%25253DUS%2525253ASC%2525253A%25252520SellerCentralLogin%252526pidt%25253D1%252526oid%25253D%252525A0%252525A0Sign%25252520in%252525A0%252525A0%2525250A%252526oidt%25253D3%252526ot%25253DSUBMIT%3B; skin=noskin; ubid-main=178-2834543-3947633; session-id-time=2082787201l; session-id=177-4413589-2799362; csm-hit=1NA2Q8GBR6KY4Y0DRT74+s-0DPXK2MT9GHVFV143098|1444301549284""",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest"
        },
        "url": "http://www.amazon.co.uk/gp/aag/ajax/searchResultsJson.html"
    }
}


BRAND_SHOP = ["1387", "1388", "2300", "2340", "2345", "2806", "2833", "2834", "2864", "2863", "3090", "3253", "3351",
              "3379", "3380", "3384", "2835", "3383", "3404", "3405", "3406", "3407", "3410", "3411", "3412", "3413",
              "3414", "3368"]

CONDITIONS = ['New', 'UsedLikeNew', 'UsedVeryGood', 'UsedGood', 'UsedAcceptable', 'CollectibleLikeNew',
              'CollectibleVeryGood', 'CollectibleGood', 'CollectibleAcceptable', 'Refurbished', 'Club']

SPECIAL_UPC = {
    '888060': {'specifics': ['MfrPartNumber'], 'pin': u'us-video_games'},
    '884226': {'specifics': ['MfrPartNumber', "ModelNumber"], 'pin': u'us-music'},
    '748807': {'specifics': ['MfrPartNumber'], 'pin': u'us-baby'},
    '866069': {'specifics': ['MfrPartNumber'], 'pin': u'uk-auto'},
    '707660': {'specifics': ['MfrPartNumber'], 'pin': u'us-office'},
    '771479': {'specifics': ['MfrPartNumber'], 'pin': u'uk-sports'},
    '767376': {'specifics': ['MfrPartNumber'], 'pin': u'uk-jewelry'},
    '782436': {'specifics': ['MfrPartNumber'], 'pin': u'uk-pet'},
    '781903': {'specifics': ['MfrPartNumber'], 'pin': u'uk-watch'},
    '739570': {'specifics': ['MfrPartNumber'], 'pin': u'us-watches'},
    '867430': {'specifics': ['MfrPartNumber'], 'pin': u'us-health'},
    '708573': {'specifics': ["MfrPartNumber", "ModelNumber"], 'pin': u'us-shoes'},
    '662498': {'specifics': ['MfrPartNumber'], 'pin': u'us-home'},
    '729695': {'specifics': ['MfrPartNumber'], 'pin': u'us-beauty'},
    '734535': {'specifics': ['MfrPartNumber', "ModelNumber"], 'pin': u'uk-clothing'},
    '752626': {'specifics': ['MfrPartNumber'], 'pin': u'us-home-garden'},
    '764592': {'specifics': ['MfrPartNumber'], 'pin': u'jp-watch'},
    '782829': {'specifics': ['MfrPartNumber'], 'pin': u'uk-baby'},
    '734479': {'specifics': ['MfrPartNumber'], 'pin': u'uk-computers'},
    '739598': {'specifics': ['MfrPartNumber'], 'pin': u'us-home-improvement'},
    '764510': {'specifics': ['MfrPartNumber'], 'pin': u'jp-beauty'},
    '785509': {'specifics': ['MfrPartNumber'], 'pin': u'jp-pet'},
    '760711': {'specifics': ['MfrPartNumber'], 'pin': u'uk-home-improvement'},
    '833678': {'specifics': ['MfrPartNumber'], 'pin': u'jp-sports'},
    '833357': {'specifics': ['MfrPartNumber', "ModelNumber"], 'pin': u'jp-shoes'},
    '753560': {'specifics': ['MfrPartNumber'], 'pin': u'us-home-art'},
    '755619': {'specifics': ['MfrPartNumber'], 'pin': u'us-sports'},
    '835303': {'specifics': ['MfrPartNumber'], 'pin': u'jp-tools'},
    '658095': {'specifics': ['MfrPartNumber'], 'pin': u'us-ce'},
    '736966': {'specifics': ['MfrPartNumber'], 'pin': u'uk-ce'},
    '837451': {'specifics': ['MfrPartNumber'], 'pin': u'jp-home'},
    '781915': {'specifics': ['MfrPartNumber'], 'pin': u'uk-beauty'},
    '738703': {'specifics': ['MfrPartNumber'], 'pin': u'uk-office'},
    '739082': {'specifics': ['MfrPartNumber'], 'pin': u'uk-toys'},
    '833359': {'specifics': ['MfrPartNumber'], 'pin': u'jp-baby'},
    '837946': {'specifics': ['MfrPartNumber'], 'pin': u'jp-computers'},
    '837478': {'specifics': ['MfrPartNumber'], 'pin': u'jp-office'},
    '749234': {'specifics': ['MfrPartNumber'], 'pin': u'us-auto'},
    '741707': {'specifics': ['MfrPartNumber'], 'pin': u'us-pet'},
    '784506': {'specifics': ['MfrPartNumber', "ModelNumber"], 'pin': u'jp-clothing'},
    '755330': {'specifics': ['MfrPartNumber'], 'pin': u'us-jewelry'},
    '783587': {'specifics': ['MfrPartNumber'], 'pin': u'jp-auto'},
    '763193': {'specifics': ['MfrPartNumber'], 'pin': u'jp-ce'},
    '660153': {'specifics': ["MfrPartNumber", "ModelNumber"], 'pin': u'us-clothing'},
    '832995': {'specifics': ['MfrPartNumber'], 'pin': u'jp-jewelry'},
    '785196': {'specifics': ['MfrPartNumber'], 'pin': u'jp-toys'},
    '853702': {'specifics': ['MfrPartNumber', "ModelNumber"], 'pin': u'uk-shoes'},
    '777942': {'specifics': ['MfrPartNumber'], 'pin': u'uk-home'},
    '669711': {'specifics': ['MfrPartNumber'], 'pin': u'us-toys'},
    '873831': {'specifics': ['MfrPartNumber'], 'pin': u'uk-health'},
    '873841': {'specifics': ['MfrPartNumber'], 'pin': u'uk-lighting'},
    '874813': {'specifics': ['MfrPartNumber'], 'pin': u'jp-health'},
}

COMMON_UPS = ["ISBN", "UPC", "EAN", "PZN", "GTIN", "GCID"]

WEIGHT_UNITS = ["GR", "KG", "LB", "OZ"]

COMMON_REPORT = ['item-name', 'item-description', 'listing-id', 'seller-sku', 'price', 'quantity', 'open-date',
                 'image-url', 'item-is-marketplace', 'product-id-type', 'zshop-shipping-fee', 'item-note',
                 'item-condition', 'zshop-category1', 'zshop-browse-path', 'zshop-storefront-feature', 'asin1',
                 'asin2', 'asin3', 'will-ship-internationally', 'expedited-shipping', 'zshop-boldface', 'product-id',
                 'bid-for-featured-placement', 'add-delete', 'pending-quantity', 'fulfillment-channel']

SPECIAL_REPORT = ["item-name", "listing-id", "seller-sku", "price", "quantity", "open-date",
                  "product-id-type", "item-note", "item-condition", "will-ship-internationally",
                  "expedited-shipping", "product-id", "pending-quantity", "fulfillment-channel"]

