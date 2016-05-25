# -*- coding: utf-8 -*-

# @author: xuhe
# @date: 16/5/6
# @description: 


WISH_SIZE = {
    "Women's Apparel": ["XXS", "XS", "S", "M", "L", "XL", "XXL"],
    "Men's Apparel": ["XS", "S", "M", "L", "XL", "XXL", "XXXL", "XXXXL", "XXXXXL"],
    'Bras': [
        '30B', '30C', '30D', '32A', '32AA', '32B', '32C', '32D', '32DD', '32DDD', '34A', '34AA', '34B', '34C', '34D',
        '34DD', '34DDD', '36A', '36AA', '36B', '36C', '36D', '36DD', '36DDD', '38A', '38B', '38C', '38D', '38DD',
        '38DDD', '40B', '40C', '40D', '40DD', '40DDD', '42D', '42DD', '42DDD', '44DD', '44DDD'
    ],
    "Women's Shoes": [
        '4', '4.5', '5', '5.5', '6', '6.5', '7', '7.5', '8', '8.5', '9', '9.5', '10', '10.5', '11',
        '11.5', '12'
    ],
    "Men's Shoes": [
        '4', '4.5', '5', '5.5', '6', '6.5', '7', '7.5', '8', '8.5', '9', '9.5', '10', '10.5', '11',
        '11.5', '12', '13', '14', '15', '16'
    ],
    'Volume': [],
    'Smartphones/Tablets': [
        'Apple Watch 38mm', 'Apple Watch 42mm', 'iPod Touch 4', 'iPod Touch 5', 'iPad Mini',
        'iPad Mini 2', 'iPad Mini 3', 'iPad Mini 4', 'iPad Air', 'iPad Air 2', 'iPad 1', 'iPad 2',
        'iPad 3', 'iPad 4', 'iPhone 4', 'iPhone 4s', 'iPhone 5', 'iPhone 5c', 'iPhone 5s', 'iPhone 6',
        'iPhone 6 Plus', 'iPhone 6S', 'iPhone 6S Plus', 'Samsung Galaxy S2', 'Samsung Galaxy S3',
        'Samsung Galaxy S3 Mini', 'Samsung Galaxy S4 Mini', 'Samsung Galaxy S4',
        'Samsung Galaxy S5 Mini', 'Samsung Galaxy S5', 'Samsung Galaxy S5 Active',
        'Samsung Galaxy S5 (E5000)', 'Samsung Galaxy S6', 'Samsung Galaxy S6 Active',
        'Samsung Galaxy S6 Edge', 'Samsung Galaxy S6 Edge Plus', 'Samsung Galaxy Mega 6.3',
        'Samsung Galaxy Note Edge N9150', 'Samsung Galaxy Note 1', 'Samsung Galaxy Note 2',
        'Samsung Galaxy Note 3', 'Samsung Galaxy Note 3 Lite N7506', 'Samsung Galaxy Note 3 Neo',
        'Samsung Galaxy Note 4', 'Samsung Galaxy Note 5', 'Samsung Galaxy Note 8.0',
        'Samsung Galaxy Note 10', 'Samsung Galaxy Tab 4.7in', 'Samsung Galaxy Tab 4.8in',
        'Samsung Galaxy A3', 'Samsung Galaxy A5', 'Samsung Galaxy A7', 'Samsung Galaxy A8',
        'Samsung Galaxy J1', 'Samsung Galaxy Alpha G850', 'Samsung Galaxy Mega 5.8',
        'Samsung Galaxy Mega 2', 'Samsung Galaxy Grand Neo', 'Samsung Galaxy Grand Prime',
        'Samsung Galaxy Grand 2', 'Samsung Galaxy Core Max',
        'Samsung Galaxy Grand Prime LTE G530H G530F', 'Samsung Galaxy Core Prime G360P',
        'Samsung Google Nexus 10', 'Samsung Tab Pro 8.4', 'Samsung Note Pro 12.2',
        'Samsung Tab 3 7.0', 'Samsung Tab 3 Lite 7.0', 'Samsung Tab 3V', 'Samsung Tab A 8.0',
        'Samsung Tab A 9.7', 'Samsung Tab S 8.4', 'Samsung Tab S 10.5', 'Samsung Tab S2 8.0',
        'Samsung Tab S2 9.7', 'Samsung Tab E 9.6', 'Amazon Kindle', 'Amazon Kindle 2',
        'Amazon Kindle DX', 'Amazon Kindle Keyboard', 'Amazon Kindle 4', 'Amazon Kindle Fire',
        'Amazon Kindle Fire PaperWhite', 'Amazon Kindle Touch', 'Amazon Kindle Fire HD 7in',
        'Amazon Kindle Fire HD 8.9in', 'Amazon Kindle Paperwhite', 'Amazon Kindle Voyage', 'HTC M7',
        'HTC M8', 'HTC M9', 'HTC One Max', 'HTC One Mini 2', 'HTC One M8 Mini', 'HTC One M9',
        'HTC One M9+', 'HTC One E8', 'HTC One E9', 'HTC One E9+', 'HTC Desire 626', 'HTC Desire 816',
        'HTC Desire 820', 'HTC Desire 826', 'SONY 339H', 'SONY L36H', 'SONY L39H', 'SONY L39U',
        'SONY Xperia C3', 'SONY Xperia E3', 'SONY Xperia M2', 'SONY Xperia T2 Ultra',
        'SONY Xperia T3', 'SONY Xperia Z2', 'SONY Xperia Z2 tablet', 'SONY Xperia Z3',
        'SONY Xperia Z3 Mini', 'SONY Xperia Z4', 'LG NEXUS 5', 'LG G2', 'LG G3', 'LG G4',
        'LG G Stylo', 'LG L40', 'LG L70', 'LG L80', 'LG L90', 'LG Tribute 2 Leon C40', 'LG L15G',
        'LG Lancet VW820', 'LG Magna H502G VOLT 2', 'LG Revere 3 / VN170', 'Nokia Lumia 640',
        'Nokia Lumia 930', 'Motorola Moto G', 'Motorola Moto G2', 'Motorola Moto G3',
        'Motorola Moto X', 'Motorola Moto X Style Pure Edition', 'Microsoft Surface RT Pro', 'iOS',
        'Huawei Ascend P6', 'Huawei Ascend 7', 'Huawei Ascend Mate 7', 'Huawei Ascend G530',
        'Huawei Honor 6', 'Huawei Honor 3c', 'Huawei Raven LTE H892L',
        'Huawei Pronto LTE SnapTO H891L G620', 'Huawei Tribute Fusion 3 Y536', 'XiaoMi Mi 3',
        'XiaoMi Mi 4', 'XiaoMi RedMi', 'XiaoMi RedMi Note', 'Android', 'Kyocera Hydro Wave C6740',
        'Alcatel onetouch Pop Astro 5042T', 'Alcatel Pop Icon 2 A846L', 'Asus Zenfone 2e',
        'ZTE LEVER Z936L', 'ZTE Speed/N9130', 'ZTE Warp Elite N9518', 'ZTE Zephyr Z752C SONATA 2'
    ],
    'Headphones': [
        'Beats Pro', 'Beats Solo', 'Beats Solo 2', 'Beats Solo 2 Wireless', 'Beats Solo-HD', 'Beats Studio',
        'Beats Studio 2013+ Models', 'Beats MIXR', 'Beats Wireless'
    ],
    'Shoes': [
        '0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5', '5.5', '6', '6.5', '7', '7.5', '8', '8.5',
        '9', '9.5', '10', '10.5', '11', '11.5', '12', '12.5', '13', '13.5', '14', '14.5', '15', '15.5', '16', '16.5',
        '17', '17.5', '18', '18.5', '19', '19.5', '20', '20.5'
    ],
    'Weight': [],
    'Area': [],
    'Additional Apparel Sizes': [
        'One Size', 'XXXS', '6XL', '7XL', '8XL', '1X', '2X', '3X', 'Youth XL(16-18)',
        'Youth L(14-16)', 'Youth M(10-12)', 'Youth S(6-8)', 'Adult', 'Kid'
    ],
    'Memory': ['1GB', '2GB', '4GB', '8GB', '16GB', '32GB', '64GB', '128GB', '256GB', '512GB', '1TB'],
    'Shapes': ['Pearl', 'Cubic', 'Heart', 'Rose', 'Basic', 'Twist'],
    'Length': [],
    'Voltage': [],
    'Others': ['MousePad Foam Backed', 'MousePad Stick it', 'Pack of 4', 'Pack of 6'],
    'MacBooks': [
        '11" MacBook', '11" MacBook Air', '12" MacBook', '13" White MacBook', '13" MacBook Air', '15" MacBook Air',
        '13" MacBook Pro', '13" MacBook Pro with Retina display', '15" MacBook Pro',
        '15" MacBook Pro with Retina display', '17" MacBook Pro'
    ],
    'Infant/Child': [
        'Newborn', '2t', '3t', '4t', '5t', '6t', '7t', '8t', '6 Months', '12 Months', '18 Months', '0-3m',
        '0-6m', '3-6m', '6-12m', '6-9m', '9-12m', '12-18m', '18-24m', '1-2 Years', '2-3 Years', '3-4 Years',
        '4-5 Years', '5-6 Years', '6-7 Years', '7-8 Years', '8-9 Years', '9-10 Years', '10-11 Years',
        '11-12 Years', '12-13 Years', '13-14 Years', '14-15 Years'
    ],
    'Infant/Child Shoes': ['7 - 8', '9 - 10', '11 - 12', '13 - 1', '2 - 3'],
    'Bedding': ['Single', 'Twin', 'Double', 'Queen', 'King', 'Super King', 'California King'],
    'Gaming': [
        'Playstation 3 Slim', 'Playstation 3 Original', 'Playstation 3 Slim 1', 'Playstation 3 Slim 2',
        'Playstation 3 Original 1', 'Playstation 3 Original 2'],
    'Numbers': [
        '0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5', '5.5', '6', '6.5', '7', '7.5', '8', '8.5',
        '9', '9.5', '10', '10.5', '11', '11.5', '12', '12.5', '13', '13.5', '14', '14.5', '15', '15.5', '16',
        '16.5', '17', '17.5', '18', '18.5', '19', '19.5', '20', '20.5'
    ],
    'Wattage': []
}

WISH_SIZE_TEXT = {
    '11': {
        'Name': 'Area', 'Value': []
    },
    '10': {
        'Name': 'Others',
        'Value': [
            ['mousepadfoambacked', 'MousePad Foam Backed'], ['mousepadstickit', 'MousePad Stick it'],
            ['packof4', 'Pack of 4'], ['packof6', 'Pack of 6']
        ]
    },
    '13': {
        'Name': 'Length',
        'Value': []
    },
    '12': {
        'Name': 'Memory',
        'Value': [
            ['1gb', '1GB'], ['2gb', '2GB'], ['4gb', '4GB'], ['8gb', '8GB'], ['16gb', '16GB'], ['32gb', '32GB'],
            ['64gb', '64GB'], ['128gb', '128GB'], ['256gb', '256GB'], ['512gb', '512GB'], ['1tb', '1TB']
        ]
    },
    '15': {
        'Name': 'Voltage', 'Value': []
    },
    '21': {
        'Name': 'Additional Apparel Sizes',
        'Value': [
            ['onesize', 'One Size'], ['xxxs', 'XXXS'], ['6xl', '6XL'], ['7xl', '7XL'], ['8xl', '8XL'],
            ['1x', '1X'], ['2x', '2X'], ['3x', '3X'], ['youthxl(16-18)', 'Youth XL(16-18)'],
            ['youthl(14-16)', 'Youth L(14-16)'], ['youthm(10-12)', 'Youth M(10-12)'], ['youths(6-8)', 'Youth S(6-8)'],
            ['adult', 'Adult'], ['kid', 'Kid']
        ]
    },
    '17': {
        'Name': 'Shoes',
        'Value': [
            ['0', '0'], ['0.5', '0.5'], ['1', '1'], ['1.5', '1.5'], ['2', '2'], ['2.5', '2.5'], ['3', '3'],
            ['3.5', '3.5'], ['4', '4'], ['4.5', '4.5'], ['5', '5'], ['5.5', '5.5'], ['6', '6'], ['6.5', '6.5'],
            ['7', '7'], ['7.5', '7.5'], ['8', '8'], ['8.5', '8.5'], ['9', '9'], ['9.5', '9.5'], ['10', '10'],
            ['10.5', '10.5'], ['11', '11'], ['11.5', '11.5'], ['12', '12'], ['12.5', '12.5'], ['13', '13'],
            ['13.5', '13.5'], ['14', '14'], ['14.5', '14.5'], ['15', '15'], ['15.5', '15.5'], ['16', '16'],
            ['16.5', '16.5'], ['17', '17'], ['17.5', '17.5'], ['18', '18'], ['18.5', '18.5'], ['19', '19'],
            ['19.5', '19.5'], ['20', '20'], ['20.5', '20.5']
        ]
    },
    '16': {
        'Name': 'Weight', 'Value': []
    },
    '22': {
        'Name': 'Infant/Child Shoes',
        'Value': [
            ['7-8', '7 - 8'], ['9-10', '9 - 10'], ['11-12', '11 - 12'], ['13-1', '13 - 1'], ['2-3', '2 - 3']
        ]
    },
    '20': {
        'Name': 'Shapes',
        'Value': [
            ['pearl', 'Pearl'], ['cubic', 'Cubic'], ['heart', 'Heart'], ['rose', 'Rose'], ['basic', 'Basic'],
            ['twist', 'Twist']
        ]
    },
    '0': {
        'Name': 'Numbers',
        'Value': [
            ['0', '0'], ['0.5', '0.5'], ['1', '1'], ['1.5', '1.5'], ['2', '2'], ['2.5', '2.5'], ['3', '3'],
            ['3.5', '3.5'], ['4', '4'], ['4.5', '4.5'], ['5', '5'], ['5.5', '5.5'], ['6', '6'], ['6.5', '6.5'],
            ['7', '7'], ['7.5', '7.5'], ['8', '8'], ['8.5', '8.5'], ['9', '9'], ['9.5', '9.5'], ['10', '10'],
            ['10.5', '10.5'], ['11', '11'], ['11.5', '11.5'], ['12', '12'], ['12.5', '12.5'], ['13', '13'],
            ['13.5', '13.5'], ['14', '14'], ['14.5', '14.5'], ['15', '15'], ['15.5', '15.5'], ['16', '16'],
            ['16.5', '16.5'], ['17', '17'], ['17.5', '17.5'], ['18', '18'], ['18.5', '18.5'], ['19', '19'],
            ['19.5', '19.5'], ['20', '20'], ['20.5', '20.5']
        ]
    },
    '3': {
        'Name': 'Bedding',
        'Value': [
            ['single', 'Single'], ['twin', 'Twin'], ['double', 'Double'], ['full', 'Queen'], ['king', 'King'],
            ['superking', 'Super King'], ['californiaking', 'California King']
        ]
    },
    '5': {
        'Name': 'Infant/Child',
        'Value': [
            ['newborn', 'Newborn'], ['2t', '2t'], ['3t', '3t'], ['4t', '4t'], ['5t', '5t'], ['6t', '6t'],
            ['7t', '7t'], ['8t', '8t'], ['6months', '6 Months'], ['12months', '12 Months'],
            ['18months', '18 Months'], ['0-3m', '0-3m'], ['0-6m', '0-6m'], ['3-6m', '3-6m'], ['6-12m', '6-12m'],
            ['6-9m', '6-9m'], ['9-12m', '9-12m'], ['12-18m', '12-18m'], ['18-24m', '18-24m'],
            ['1-2years', '1-2 Years'], ['2-3years', '2-3 Years'], ['3-4years', '3-4 Years'],
            ['4-5years', '4-5 Years'], ['5-6years', '5-6 Years'], ['6-7years', '6-7 Years'],
            ['7-8years', '7-8 Years'], ['8-9years', '8-9 Years'], ['9-10years', '9-10 Years'],
            ['10-11years', '10-11 Years'], ['11-12years', '11-12 Years'], ['12-13years', '12-13 Years'],
            ['13-14years', '13-14 Years'], ['14-15years', '14-15 Years']
        ]
    },
    '4': {
        'Name': 'Bras',
        'Value': [
            ['30b', '30B'], ['30c', '30C'], ['30d', '30D'], ['32a', '32A'], ['32aa', '32AA'], ['32b', '32B'],
            ['32c', '32C'], ['32d', '32D'], ['32dd', '32DD'], ['32ddd', '32DDD'], ['34a', '34A'], ['34aa', '34AA'],
            ['34b', '34B'], ['34c', '34C'], ['34d', '34D'], ['34dd', '34DD'], ['34ddd', '34DDD'], ['36a', '36A'],
            ['36aa', '36AA'], ['36b', '36B'], ['36c', '36C'], ['36d', '36D'], ['36dd', '36DD'], ['36ddd', '36DDD'],
            ['38a', '38A'], ['38b', '38B'], ['38c', '38C'], ['38d', '38D'], ['38dd', '38DD'], ['38ddd', '38DDD'],
            ['40b', '40B'], ['40c', '40C'], ['40d', '40D'], ['40dd', '40DD'], ['40ddd', '40DDD'], ['42d', '42D'],
            ['42dd', '42DD'], ['42ddd', '42DDD'], ['44dd', '44DD'], ['44ddd', '44DDD']
        ]
    },
    '7': {
        'Name': 'Smartphones/Tablets',
        'Value': [
            ['applewatch38mm', 'Apple Watch 38mm'], ['applewatch42mm', 'Apple Watch 42mm'],
            ['ipodtouch4', 'iPod Touch 4'], ['ipodtouch5', 'iPod Touch 5'], ['ipadmini', 'iPad Mini'],
            ['ipadmini2', 'iPad Mini 2'], ['ipadmini3', 'iPad Mini 3'], ['ipadmini4', 'iPad Mini 4'],
            ['ipadair', 'iPad Air'], ['ipadair2', 'iPad Air 2'], ['ipad1', 'iPad 1'], ['ipad2', 'iPad 2'],
            ['ipad3', 'iPad 3'], ['ipad4', 'iPad 4'], ['iphone4', 'iPhone 4'], ['iphone4s', 'iPhone 4s'],
            ['iphone5', 'iPhone 5'], ['iphone5c', 'iPhone 5c'], ['iphone5s', 'iPhone 5s'], ['iphone6', 'iPhone 6'],
            ['iphone6plus', 'iPhone 6 Plus'], ['iphone6s', 'iPhone 6S'], ['iphone6splus', 'iPhone 6S Plus'],
            ['samsunggalaxys2', 'Samsung Galaxy S2'], ['samsunggalaxys3', 'Samsung Galaxy S3'],
            ['samsunggalaxys3mini', 'Samsung Galaxy S3 Mini'], ['samsunggalaxys4mini', 'Samsung Galaxy S4 Mini'],
            ['samsunggalaxys4', 'Samsung Galaxy S4'], ['samsunggalaxys5mini', 'Samsung Galaxy S5 Mini'],
            ['samsunggalaxys5', 'Samsung Galaxy S5'], ['samsunggalaxys5active', 'Samsung Galaxy S5 Active'],
            ['samsunggalaxys5(e5000)', 'Samsung Galaxy S5 (E5000)'], ['samsunggalaxys6', 'Samsung Galaxy S6'],
            ['samsunggalaxys6active', 'Samsung Galaxy S6 Active'], ['samsunggalaxys6edge', 'Samsung Galaxy S6 Edge'],
            ['samsunggalaxys6edgeplus', 'Samsung Galaxy S6 Edge Plus'],
            ['samsunggalaxymega6.3', 'Samsung Galaxy Mega 6.3'],
            ['samsunggalaxynoteedgen9150', 'Samsung Galaxy Note Edge N9150'],
            ['samsunggalaxynote1', 'Samsung Galaxy Note 1'], ['samsunggalaxynote2', 'Samsung Galaxy Note 2'],
            ['samsunggalaxynote3', 'Samsung Galaxy Note 3'],
            ['samsunggalaxynote3liten7506', 'Samsung Galaxy Note 3 Lite N7506'],
            ['samsunggalaxynote3neo', 'Samsung Galaxy Note 3 Neo'], ['samsunggalaxynote4', 'Samsung Galaxy Note 4'],
            ['samsunggalaxynote5', 'Samsung Galaxy Note 5'], ['samsunggalaxynote8.0', 'Samsung Galaxy Note 8.0'],
            ['samsunggalaxynote10', 'Samsung Galaxy Note 10'], ['samsunggalaxytab4.7in', 'Samsung Galaxy Tab 4.7in'],
            ['samsunggalaxytab4.8in', 'Samsung Galaxy Tab 4.8in'], ['samsunggalaxya3', 'Samsung Galaxy A3'],
            ['samsunggalaxya5', 'Samsung Galaxy A5'], ['samsunggalaxya7', 'Samsung Galaxy A7'],
            ['samsunggalaxya8', 'Samsung Galaxy A8'], ['samsunggalaxyj1', 'Samsung Galaxy J1'],
            ['samsunggalaxyalphag850', 'Samsung Galaxy Alpha G850'],
            ['samsunggalaxymega5.8', 'Samsung Galaxy Mega 5.8'], ['samsunggalaxymega2', 'Samsung Galaxy Mega 2'],
            ['samsunggalaxygrandneo', 'Samsung Galaxy Grand Neo'],
            ['samsunggalaxygrandprime', 'Samsung Galaxy Grand Prime'],
            ['samsunggalaxygrand2', 'Samsung Galaxy Grand 2'], ['samsunggalaxycoremax', 'Samsung Galaxy Core Max'],
            ['samsunggalaxygrandprimelteg530hg530f', 'Samsung Galaxy Grand Prime LTE G530H G530F'],
            ['samsunggalaxycoreprimeg360p', 'Samsung Galaxy Core Prime G360P'],
            ['samsunggooglenexus10', 'Samsung Google Nexus 10'], ['samsungtabpro8.4', 'Samsung Tab Pro 8.4'],
            ['samsungnotepro12.2', 'Samsung Note Pro 12.2'], ['samsungtab37.0', 'Samsung Tab 3 7.0'],
            ['samsungtab3lite7.0', 'Samsung Tab 3 Lite 7.0'], ['samsungtab3v', 'Samsung Tab 3V'],
            ['samsungtaba8.0', 'Samsung Tab A 8.0'], ['samsungtaba9.7', 'Samsung Tab A 9.7'],
            ['samsungtabs8.4', 'Samsung Tab S 8.4'], ['samsungtabs10.5', 'Samsung Tab S 10.5'],
            ['samsungtabs28.0', 'Samsung Tab S2 8.0'], ['samsungtabs29.7', 'Samsung Tab S2 9.7'],
            ['samsungtabe9.6', 'Samsung Tab E 9.6'], ['amazonkindle', 'Amazon Kindle'],
            ['amazonkindle2', 'Amazon Kindle 2'], ['amazonkindledx', 'Amazon Kindle DX'],
            ['amazonkindlekeyboard', 'Amazon Kindle Keyboard'], ['amazonkindle4', 'Amazon Kindle 4'],
            ['amazonkindlefire', 'Amazon Kindle Fire'], ['amazonkindlefirepaperwhite', 'Amazon Kindle Fire PaperWhite'],
            ['amazonkindletouch', 'Amazon Kindle Touch'], ['amazonkindlefirehd7in', 'Amazon Kindle Fire HD 7in'],
            ['amazonkindlefirehd8.9in', 'Amazon Kindle Fire HD 8.9in'],
            ['amazonkindlepaperwhite', 'Amazon Kindle Paperwhite'], ['amazonkindlevoyage', 'Amazon Kindle Voyage'],
            ['htcm7', 'HTC M7'], ['htcm8', 'HTC M8'], ['htcm9', 'HTC M9'], ['htconemax', 'HTC One Max'],
            ['htconemini2', 'HTC One Mini 2'], ['htconem8mini', 'HTC One M8 Mini'], ['htconem9', 'HTC One M9'],
            ['htconem9+', 'HTC One M9+'], ['htconee8', 'HTC One E8'], ['htconee9', 'HTC One E9'],
            ['htconee9+', 'HTC One E9+'], ['htcdesire626', 'HTC Desire 626'], ['htcdesire816', 'HTC Desire 816'],
            ['htcdesire820', 'HTC Desire 820'], ['htcdesire826', 'HTC Desire 826'], ['sony339h', 'SONY 339H'],
            ['sonyl36h', 'SONY L36H'], ['sonyl39h', 'SONY L39H'], ['sonyl39u', 'SONY L39U'],
            ['sonyxperiac3', 'SONY Xperia C3'], ['sonyxperiae3', 'SONY Xperia E3'], ['sonyxperiam2', 'SONY Xperia M2'],
            ['sonyxperiat2ultra', 'SONY Xperia T2 Ultra'], ['sonyxperiat3', 'SONY Xperia T3'],
            ['sonyxperiaz2', 'SONY Xperia Z2'], ['sonyxperiaz2tablet', 'SONY Xperia Z2 tablet'],
            ['sonyxperiaz3', 'SONY Xperia Z3'], ['sonyxperiaz3mini', 'SONY Xperia Z3 Mini'],
            ['sonyxperiaz4', 'SONY Xperia Z4'], ['lgnexus5', 'LG NEXUS 5'],
            ['lgg2', 'LG G2'], ['lgg3', 'LG G3'], ['lgg4', 'LG G4'], ['lggstylo', 'LG G Stylo'], ['lgl40', 'LG L40'],
            ['lgl70', 'LG L70'], ['lgl80', 'LG L80'], ['lgl90', 'LG L90'],
            ['lgtribute2leonc40', 'LG Tribute 2 Leon C40'], ['lgl15g', 'LG L15G'], ['lglancetvw820', 'LG Lancet VW820'],
            ['lgmagnah502gvolt2', 'LG Magna H502G VOLT 2'], ['lgrevere3/vn170', 'LG Revere 3 / VN170'],
            ['nokialumia640', 'Nokia Lumia 640'], ['nokialumia930', 'Nokia Lumia 930'],
            ['motorolamotog', 'Motorola Moto G'], ['motorolamotog2', 'Motorola Moto G2'],
            ['motorolamotog3', 'Motorola Moto G3'], ['motorolamotox', 'Motorola Moto X'],
            ['motorolamotoxstylepureedition', 'Motorola Moto X Style Pure Edition'],
            ['microsoftsurfacertpro', 'Microsoft Surface RT Pro'], ['ios', 'iOS'],
            ['huaweiascendp6', 'Huawei Ascend P6'], ['huaweiascendp7', 'Huawei Ascend 7'],
            ['huaweiascendmate7', 'Huawei Ascend Mate 7'], ['huaweiascendg530', 'Huawei Ascend G530'],
            ['huaweihonor6', 'Huawei Honor 6'], ['huaweihonor3c', 'Huawei Honor 3c'],
            ['huaweiravenlteh892l', 'Huawei Raven LTE H892L'],
            ['huaweiprontoltesnaptoh891lg620', 'Huawei Pronto LTE SnapTO H891L G620'],
            ['huaweitributefusion3y536', 'Huawei Tribute Fusion 3 Y536'], ['xiaomimi3', 'XiaoMi Mi 3'],
            ['xiaomimi4', 'XiaoMi Mi 4'], ['xiaomiredmi', 'XiaoMi RedMi'], ['xiaomiredminote', 'XiaoMi RedMi Note'],
            ['android', 'Android'], ['kyocerahydrowavec6740', 'Kyocera Hydro Wave C6740'],
            ['alcatelonetouchpopastro5042t', 'Alcatel onetouch Pop Astro 5042T'],
            ['alcatelpopicon2a846l', 'Alcatel Pop Icon 2 A846L'], ['asuszenfone2e', 'Asus Zenfone 2e'],
            ['zteleverz936l', 'ZTE LEVER Z936L'], ['ztespeed/n9130', 'ZTE Speed/N9130'],
            ['ztewarpeliten9518', 'ZTE Warp Elite N9518'], ['ztezephyrz752csonata2', 'ZTE Zephyr Z752C SONATA 2']
        ]
    },
    '6': {
        'Name': 'MacBooks',
        'Value': [
            ['11"macbook', '11" MacBook'], ['11"macbookair', '11" MacBook Air'], ['12"macbook', '12" MacBook'],
            ['13"whitemacbook', '13" White MacBook'], ['13"macbookair', '13" MacBook Air'],
            ['15"macbookair', '15" MacBook Air'], ['13"macbookpro', '13" MacBook Pro'],
            ['13"macbookprowithretinadisplay', '13" MacBook Pro with Retina display'],
            ['15"macbookpro', '15" MacBook Pro'],
            ['15"macbookprowithretinadisplay', '15" MacBook Pro with Retina display'],
            ['17"macbookpro', '17" MacBook Pro']
        ]
    },
    '9': {
        'Name': 'Headphones',
        'Value': [
            ['beatspro', 'Beats Pro'], ['beatssolo', 'Beats Solo'], ['beatssolo2', 'Beats Solo 2'],
            ['beatssolo2wireless', 'Beats Solo 2 Wireless'], ['beatssolo-hd', 'Beats Solo-HD'],
            ['beatsstudio', 'Beats Studio'], ['beatsstudio2013+models', 'Beats Studio 2013+ Models'],
            ['beatsmixr', 'Beats MIXR'], ['beatswireless', 'Beats Wireless']
        ]
    },
    '8': {
        'Name': 'Gaming',
        'Value': [
            ['playstation3slim', 'Playstation 3 Slim'], ['playstation3original', 'Playstation 3 Original'],
            ['playstation3slim1', 'Playstation 3 Slim 1'], ['playstation3slim2', 'Playstation 3 Slim 2'],
            ['playstation3original1', 'Playstation 3 Original 1'], ['playstation3original2', 'Playstation 3 Original 2']
        ]
    },
    '14': {
        'Name': 'Volume',
        'Value': []
    },
    '23': {
        'Name': 'Wattage',
        'Value': []
    },
    '24': {

    }
}

WISH_COLOR = [
    "abyss", "acid blue", "acid green", "aero", "aero blue", "african purple", "air force blue", "alabama crimson",
    "alaska blue", "alice blue", "alizarin crimson", "alloy orange", "almond", "amaranth", "amaranth pink",
    "amarillo", "amazon", "amber", "amber gold", "ambrosial crush", "american rose", "amethyst", "android green",
    "antique black", "antique gold", "antique brass", "antique bronze", "antique fuchsia", "antique ruby",
    "antique silver", "antique white", "apple green", "apricot", "aqua", "aqua blue", "aquamarine", "arctic blue",
    "army green", "arsenic", "arylide yellow", "ash black", "ash grey", "asparagus", "asphalt", "atomic tangerine",
    "auburn", "aureolin", "aurometalsaurus", "avocado", "azure", "azure mist", "b'dazzled blue", "baby doll",
    "baby blue", "baby blue eyes", "baby pink", "baby powder", "ball blue", "banana mania", "banana yellow",
    "barbie pink", "barn red", "battleship grey", "bazaar", "beau blue", "beaver", "beige", "berry", "big dip o'ruby",
    "birch", "bisque", "bistre", "bistre brown", "bitter lemon", "bitter lime", "bittersweet", "bittersweet shimmer",
    "black", "black bean", "black brown", "black fuchsia", "black gray", "black leather jacket", "black olive",
    "black white", "blanched almond", "bleu de france", "blizzard blue", "blond", "blue", "blue bell",
    "blue chocolate", "blue light wash", "blue wash", "blue sapphire", "blue yonder", "blueberry", "bluebonnet",
    "blush", "bole", "bondi blue", "bone", "bottle green", "boysenberry", "brandeis blue", "brass", "brick red",
    "bright orange", "bright blue", "bright cerulean", "bright green", "bright lavender", "bright maroon",
    "bright navy blue", "bright pink", "bright red", "bright turquoise", "bright ube", "brilliant lavender",
    "brilliant rose", "brink pink", "british racing green", "bronze", "bronze yellow", "brown", "brown sugar",
    "brunswick green", "bubble gum", "bubblegum pink", "bubbles", "bud green", "buff", "bulgarian rose", "burgundy",
    "burgundy metallic", "burgundy pearl", "burlywood", "burnt orange", "burnt sienna", "burnt umber", "byzantine",
    "byzantium", "cg blue", "cg red", "cadet", "cadet blue", "cadet grey", "cadmium green", "cadmium orange",
    "cadmium red", "cadmium yellow", "cafe", "cal poly green", "calm", "cambridge blue", "camel", "camel brown",
    "cameo pink", "camouflage", "camouflage green", "canary yellow", "candy apple red", "candy pink", "capri",
    "caput mortuum", "carbon fiber black", "cardinal", "caribbean green", "carmine", "carmine pink", "carmine red",
    "carnation pink", "carnelian", "carolina blue", "carrot orange", "castleton green", "catalina blue", "catawba",
    "cedar chest", "ceil", "celadon", "celadon blue", "celadon green", "celery green", "celeste", "celestial blue",
    "cerise", "cerise pink", "cerulean", "cerulean blue", "cerulean frost", "chamoisee", "champagne", "charcoal",
    "charleston green", "charm pink", "chartreuse", "checkered red", "checkered white", "cheddar yellow", "cheers",
    "cheetah", "cheetah print", "cherry", "cherry pink", "cherry blossom pink", "chestnut", "china pink",
    "china rose", "chinese red", "chinese violet", "chocolate", "chocolate brown", "chrome yellow", "cinereous",
    "cinnabar", "cinnamon", "citrine", "citron", "claret", "classic rose", "clear", "clear beige", "clear blue",
    "clear gray", "clear green", "clear green pearl", "clear pink", "clear pink pearl", "cobalt", "cocoa",
    "cocoa bean", "cocoa brown", "coconut", "coffee", "coffee bean silver pink", "columbia blue", "congo pink",
    "cool black", "cool grey", "cool white", "copper", "copper penny", "copper red", "copper rose", "coquelicot",
    "coral", "coral green", "coral pink", "coral red", "cordovan", "corn", "cornell red", "cornflower blue",
    "cornsilk", "cosmic latte", "cotton candy", "cream", "crimson", "crimson glory", "crystal ball", "crystal clear",
    "cyan", "cyber grape", "cyber yellow", "daffodil", "dahlia", "dandelion", "dark blue pearl", "dark army green",
    "dark blond", "dark blue", "dark brown", "dark byzantium", "dark candy apple red", "dark cerulean",
    "dark chestnut", "dark coffee", "dark coral", "dark cyan", "dark electric blue", "dark goldenrod", "dark gray",
    "dark green", "dark grey", "dark imperial blue", "dark jungle green", "dark khaki", "dark lava", "dark lavender",
    "dark liver", "dark magenta", "dark midnight blue", "dark moss green", "dark olive green", "dark orange",
    "dark orchid", "dark pastel blue", "dark pastel green", "dark pastel purple", "dark pastel red", "dark pink",
    "dark plum", "dark powder blue", "dark purple", "dark raspberry", "dark red", "dark salmon", "dark scarlet",
    "dark sea green", "dark sienna", "dark sky blue", "dark slate blue", "dark slate gray", "dark spring green",
    "dark tan", "dark tangerine", "dark taupe", "dark terra cotta", "dark turquoise", "dark vanilla", "dark violet",
    "dark yellow", "dartmouth green", "davy's grey", "debian red", "deep", "deep space sparkle", "deep taupe",
    "deep tuscan red", "deep carmine", "deep carmine pink", "deep carrot orange", "deep cerise", "deep champagne",
    "deep chestnut", "deep coffee", "deep fuchsia", "deep jungle green", "deep lemon", "deep lilac", "deep magenta",
    "deep mauve", "deep moss green", "deep peach", "deep pink", "deep ruby", "deep saffron", "deep sky blue", "deer",
    "denim", "denim blue", "desert", "desert sand", "desire", "diamond", "dim gray", "dinar", "dirt", "dodger blue",
    "dogwood rose", "dollar bill", "donkey brown", "drab", "dreamscape", "duke blue", "dust storm", "dutch white",
    "earth", "earth yellow", "ebony", "ecru", "eggplant", "eggshell", "egyptian blue", "electric blue",
    "electric crimson", "electric cyan", "electric green", "electric indigo", "electric lavender", "electric lime",
    "electric purple", "electric ultramarine", "electric violet", "electric yellow", "emerald", "eminence", "emotion",
    "english green", "english lavender", "english red", "english violet", "eton blue", "eucalyptus", "fabulous",
    "fallow", "falu red", "fandango", "fandango pink", "fashion fuchsia", "fawn", "feldgrau", "feldspar",
    "fern green", "ferrari red", "field drab", "fire engine red", "firebrick", "flame", "flamingo pink",
    "flat dark earth", "flattery", "flavescent", "flax", "flirt", "floral", "floral print", "floral white",
    "fluorescence green", "fluorescent blue", "fluorescent green", "fluorescent orange", "fluorescent pink",
    "fluorescent rose", "fluorescent yellow", "flush", "folly", "forest camouflage", "forest green", "french beige",
    "french bistre", "french blue", "french lilac", "french lime", "french mauve", "french puce", "french raspberry",
    "french rose", "french sky blue", "french wine", "fresh air", "frost white", "fuchsia", "fuchsia pink",
    "fuchsia rose", "fulvous", "fushcia", "fuzzy wuzzy", "gainsboro", "gamboge", "garnet", "generic viridian",
    "ghost white", "giants orange", "ginger", "giraffe", "glaucous", "glistening sun", "glitter", "gold",
    "gold fusion", "golden", "golden brown", "golden poppy", "golden yellow", "goldenrod", "goldfish", "goldmine",
    "gradient black", "granny smith apple", "grape", "grass green", "gray", "green", "green apple", "green pearl",
    "green light", "green plaid", "grey", "grey white", "greyish white", "grullo", "guppie green", "han blue",
    "han purple", "hansa yellow", "harlequin", "harvard crimson", "harvest gold", "heart gold", "heather gray",
    "heather grey", "heliotrope", "highlight", "hollywood cerise", "honey", "honeydew", "honolulu blue",
    "hot magenta", "hot pink", "hunter green", "iceberg", "icterine", "illuminating emerald", "imperial",
    "imperial blue", "imperial purple", "imperial red", "inchworm", "independence", "india green", "indian red",
    "indian yellow", "indigo", "indigo dye", "ink blue", "iridescent", "iris", "irish green", "irresistible",
    "isabelline", "islamic green", "italian sky blue", "ivory", "jade", "japanese indigo", "japanese violet",
    "jasmine", "jasper", "jazzberry jam", "jelly bean", "jet", "jonquil", "june bud", "jungle green", "ku crimson",
    "kelly green", "kenyan copper", "keppel", "khaki", "khaki beige", "khaki green", "kobe", "kobi", "kombu green",
    "la salle green", "lake blue", "lake green", "languid lavender", "lapis lazuli", "laser lemon", "latte",
    "laurel green", "lava", "lavender", "lavender blue", "lavender blush", "lavender gray", "lavender indigo",
    "lavender magenta", "lavender mist", "lavender pink", "lavender purple", "lavender rose", "lawn green", "leaf",
    "lemon", "lemon chiffon", "lemon curry", "lemon glacier", "lemon lime", "lemon meringue", "lemon yellow",
    "leopard", "leopard print", "liberty", "licorice", "light blue pearl", "light thulian pink", "light apricot",
    "light beige", "light blond", "light blue", "light brown", "light carmine pink", "light coffee", "light coral",
    "light cornflower blue", "light crimson", "light cyan", "light fuchsia pink", "light goldenrod yellow",
    "light gray", "light green", "light grey", "light khaki", "light leopard", "light medium orchid",
    "light moss green", "light orchid", "light pastel purple", "light pink", "light purple", "light red ochre",
    "light rose", "light salmon", "light salmon pink", "light sea green", "light sky blue", "light slate gray",
    "light steel blue", "light tan", "light taupe", "light wine red", "light yellow", "lilac", "lime", "lime green",
    "limerick", "lincoln green", "linen", "lion", "little boy blue", "liver", "liver chestnut", "livid", "lollipop",
    "lumber", "lust", "msu green", "magenta", "magenta haze", "magic mint", "magnolia", "mahogany", "maize",
    "majorelle blue", "malachite", "manatee", "mango tango", "mantis", "maple", "marble", "mardi gras", "maroon",
    "matte black", "matte white", "mauve", "mauve taupe", "mauvelous", "may green", "maya blue", "meat brown",
    "medium persian blue", "medium tuscan red", "medium aquamarine", "medium blond", "medium blue", "medium brown",
    "medium candy apple red", "medium carmine", "medium champagne", "medium electric blue", "medium jungle green",
    "medium lavender magenta", "medium orchid", "medium purple", "medium ruby", "medium sea green", "medium sky blue",
    "medium slate blue", "medium spring bud", "medium spring green", "medium taupe", "medium turquoise",
    "medium vermilion", "mellow apricot", "mellow yellow", "melon", "metallic bronze", "metallic gold",
    "metallic onyx", "metallic pink", "metallic purple", "metallic red", "metallic seaweed", "metallic silver",
    "metallic sunburst", "mexican pink", "mica", "midnight", "midnight blue", "midnight green", "midori",
    "mikado yellow", "milk chocolate", "milk white", "mint", "mint cream", "mint green", "misty rose", "moccasin",
    "mode beige", "moonstone blue", "mordant red 19", "moss green", "mother of pearl", "mountain meadow",
    "mountbatten pink", "mughal green", "mulberry", "multicolor", "multicolored", "mustard", "myrtle green",
    "nacarat", "nadeshiko pink", "napier green", "naples yellow", "native earth", "natural", "navajo white", "navy",
    "navy blue", "navy purple", "neon carrot", "neon blue", "neon fuchsia", "neon green", "neon orange", "neon pink",
    "neon red", "neon yellow", "new car", "new york pink", "newspaper", "noche", "north texas green", "nude",
    "nutmeg", "nyanza", "ou crimson red", "ocean boat blue", "ocean blue", "ochre", "off white", "office green",
    "old burgundy", "old gold", "old lace", "old lavender", "old mauve", "old moss green", "old rose", "old silver",
    "olive", "olive drab", "olive green", "olive green black", "olivine", "onyx", "opera mauve", "orange",
    "orange light", "orange peel", "orange plaid", "orchid", "orchid pink", "orioles orange", "orion", "otter brown",
    "outer space", "outrageous orange", "oxford blue", "pakistan green", "palatinate blue", "palatinate purple",
    "pale aqua", "pale blue", "pale brown", "pale carmine", "pale cerulean", "pale chestnut", "pale copper",
    "pale cornflower blue", "pale gold", "pale goldenrod", "pale green", "pale lavender", "pale magenta", "pale pink",
    "pale plum", "pale robin egg blue", "pale silver", "pale spring bud", "pale taupe", "pale turquoise",
    "pansy purple", "paolo veronese green", "papaya whip", "paris green", "pastel blue", "pastel brown",
    "pastel gray", "pastel green", "pastel magenta", "pastel orange", "pastel pink", "pastel purple", "pastel red",
    "pastel violet", "pastel yellow", "patriarch", "payne's grey", "peach", "peach puff", "peacock blue",
    "peak green", "pear", "pearl", "pearl aqua", "pearl white", "pearly purple", "peridot", "periwinkle",
    "persian blue", "persian green", "persian indigo", "persian orange", "persian pink", "persian plum",
    "persian red", "persian rose", "persimmon", "peru", "phlox", "phthalo blue", "phthalo green", "pictorial carmine",
    "piggy pink", "pine green", "pink", "pink beige", "pink cheetah", "pink green", "pink purple green",
    "pink sherbet", "pink indigo", "pink lace", "pink lavender", "pink light", "pink pearl", "pinky", "pistachio",
    "platinum", "plum", "popstar", "portland orange", "powder blue", "princeton orange", "prune", "prussian blue",
    "psychedelic purple", "puce", "puce red", "pumpkin", "pure", "pure white", "purple", "purple heart",
    "purple fuchsia", "purple light", "purple mountain majesty", "purple navy", "purple pizzazz", "purple taupe",
    "purplish red", "purpureus", "quartz", "queen blue", "queen pink", "rackley", "radical red", "rajah", "raspberry",
    "raspberry glace", "raspberry pink", "raspberry rose", "raw umber", "razzle dazzle rose", "razzmatazz",
    "razzmic berry", "red", "red hot", "red pearl", "red black", "red devil", "redwood", "regalia", "resolution blue",
    "rhythm", "rich black", "rich brilliant lavender", "rich carmine", "rich electric blue", "rich lavender",
    "rich lilac", "rich maroon", "rifle green", "robin egg blue", "rocket metallic", "roman silver", "rose",
    "rose petal", "rose bonbon", "rose ebony", "rose gold", "rose madder", "rose pink", "rose quartz", "rose red",
    "rose taupe", "rose vale", "rosewood", "rosso corsa", "rosy brown", "royal azure", "royal blue", "royal fuchsia",
    "royal purple", "royal yellow", "ruber", "rubine red", "ruby", "ruby red", "ruddy", "ruddy brown", "ruddy pink",
    "rufous", "russet", "russian green", "russian violet", "rust", "rust brown", "rusty", "rusty red",
    "sacramento state green", "saddle brown", "safety orange", "safety yellow", "saffron", "salmon", "salmon pink",
    "sand", "sand dune", "sandstorm", "sandy", "sandy brown", "sandy taupe", "sangria", "sap green", "sapphire",
    "sapphire blue", "satin sheen gold", "scarlet", "schauss pink", "school bus yellow", "screamin' green", "sea",
    "sea blue", "sea green", "seal brown", "seashell", "selective yellow", "sensual", "sepia", "serenity", "shadow",
    "shampoo", "shamrock green", "sheen green", "shimmering blush", "shocking pink", "sienna", "sigal", "silver",
    "silver lake blue", "silver chalice", "silver gray", "silver green", "silver grey", "silver pink", "silver sand",
    "silver white", "sinopia", "skobeloff", "sky", "sky blue", "sky magenta", "skyblue orange", "slate", "slate blue",
    "slate gray", "smalt", "smitten", "smoke", "smokey topaz", "smoky black", "snow", "snow white", "soap",
    "sonic silver", "space cadet", "spanish bistre", "spanish blue", "spanish carmine", "spanish crimson",
    "spanish gray", "spanish orange", "spanish sky blue", "spanish viridian", "sparkling white", "spartan crimson",
    "spiro disco ball", "spring bud", "spring green", "star", "star command blue", "steel blue", "steel pink", "stem",
    "stil de grain yellow", "stizza", "stormcloud", "straw", "strawberry", "sunglow", "sunray", "sunset",
    "sunset kiss", "sunset plum", "sunset orange", "super pink", "sweet gold", "tan", "tangelo", "tangerine",
    "tangerine yellow", "tango pink", "taupe", "taupe gray", "tea green", "tea rose", "teal", "teal blue",
    "teal deer", "teal green", "telemagenta", "terra cotta", "thistle", "thulian pink", "tickle me pink",
    "tiffany blue", "tiger", "tiger print", "tiger's eye", "timberwolf", "titanium yellow", "tomato", "toolbox",
    "topaz", "tortoise", "tractor red", "transparent", "transparent black", "transparent white",
    "transparent dark green", "transparent pink", "transparent red", "trolley grey", "tropical rain forest",
    "true blue", "tufts blue", "tulip", "tumbleweed", "turkish rose", "turquoise", "turquoise black",
    "turquoise blue", "turquoise green", "tuscan", "tuscan brown", "tuscan red", "tuscan tan", "tuscany",
    "twilight lavender", "tyrian purple", "ua blue", "ua red", "ucla blue", "ucla gold", "ufo green",
    "up forest green", "up maroon", "usafa blue", "usc cardinal", "usc gold", "uv purple", "ube", "ultra",
    "ultra pink", "ultramarine", "ultramarine blue", "umber", "unbleached silk", "united nations blue",
    "unmellow yellow", "upsdell red", "urobilin", "utah crimson", "vanilla", "vanilla ice", "vegas gold",
    "velvet touch pink", "velvet touch purple", "velvet touch zebra", "venetian red", "vercafe", "verde", "verdigris",
    "vermilion", "veronica", "viola", "violet", "viridian", "viridian green", "vivid auburn", "vivid burgundy",
    "vivid cerise", "vivid orchid", "vivid sky blue", "vivid tangerine", "vivid violet", "warm yellow", "warm black",
    "warm white", "washed black", "water blue", "water wave camouflage", "watermelon red", "waterspout", "wenge",
    "wheat", "white", "white dye dip", "white glitter", "white gold", "white smoke", "wild strawberry",
    "wild watermelon", "wild blue yonder", "wild orchid", "windsor tan", "wine", "wine dregs", "wine red", "wisteria",
    "wood brown", "wow", "xanadu", "yale blue", "yankees blue", "yellow", "yellow orange", "yellow pearl",
    "yellow camouflage", "yellow light", "yellow rose", "zaffre", "zebra", "zebra print", "zinnwaldite brown", "zomp",
    "unadulterrated life"
]

WISH_SIZE_PATTERN = {
    "Area": [
        r"^(\d+(\.\d+)?)\s*(mm|cm|m|in\.?|inch(es)?|\"|\'|ft\.?|feet)\s*(\*|x|by)\s*(\d+(\.\d*)?)\s*(mm|cm|m|in\.?|inch(es)?|\"|\'|ft\.?|feet)$",
        r"^(\d+(\.\d+)?)\s*(mm|cm|m|in\.?|inch(es)?|\"|\'|ft\.?|feet)\s*(\*|x|by)\s*(\d+(\.\d*)?)\s*(mm|cm|m|in\.?|inch(es)?|\"|\'|ft\.?|feet)\s*(\*|x|X|by)\s*(\d+(\.\d*)?)\s*(mm|cm|m|in\.?|inch(es)?|\"|\'|ft\.?|feet)$"
    ],
    "Length": [
        r"^(\d+(\.\d+)?)\s*(mm|cm|m|in\.?|inch(es)?|\"|\'|ft\.?|feet)$",
        r"^(\d+(\.\d+)?)\s*(ft.?|feet|\')\s*(\d+(\.\d+)?)\s*(in\.?|inche(es)?|\")$"
    ],
    "Volume": [
        r"^(\d+(\.\d+)?)\s*(ml|l|oz\.?|m\^3|cm\^3|gallon|quart|cup|qt\.?|pt\.?|litre|liter|pint|fl\.?\s?oz\.?)s?$"
    ],
    "Voltage": [r"^(\d+(\.\d+)?)\s*v$"],
    "Weight": [r"^(\d+(\.\d+)?)\s*(ft.?|feet|\')\s*(\d+(\.\d+)?)\s*(in\.?|inche(es)?|\")$"],
    "Shoes": [r"^(\d+(\.\d+)?)\s*$"],
    "Wattage": [r"^(\d+(\.\d+)?)\s*w$"],
    "Numbers": [r"^(\d+(\.\d+)?)\s*$"]
}


import re


def get_size_type(size, *others):
    size = str(size)
    if re.compile("^((X*|\dX)[SL]|M)$").match(size.upper()):
        for other in others:
            otr = " ".join(other) if isinstance(other, list) else other
            if re.compile("(^| )wom(a|e)n([\'|\"]s|( |$))").search(otr.lower()):
                return "Women's Apparel"
            if re.compile("(^| )m(a|e)n([\'|\"]s|( |$))").search(otr.lower()):
                return "Men's Apparel"
    for addi_size in WISH_SIZE["Additional Apparel Sizes"]:
        if size.lower() == addi_size.lower():
            return "Additional Apparel Sizes"
    for size_type in [
        "Bras", "Smartphones/Tablets", "Headphones", "Bedding",
        "Memory", "Shapes", "Others", "MacBooks", "Gaming", "Infant/Child",
        "Infant/Child Shoes",
    ]:
        if size in WISH_SIZE[size_type]:
            return size_type
    if re.compile(WISH_SIZE_PATTERN["Numbers"][0]).match(size):
        for other in others:
            otr = " ".join(other) if isinstance(other, list) else other
            if re.compile("(^| )shoes?( |$)").search(otr.lower()) and size in WISH_SIZE["Shoes"]:
                return "Shoes"
        return "Numbers"
    for size_type in ["Area", "Length", "Volume", "Voltage", "Weight", "Wattage"]:
        for pattern in WISH_SIZE_PATTERN[size_type]:
            if re.compile(pattern).match(size.lower()):
                return size_type
    return "Men's Apparel"

