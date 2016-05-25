# -*- coding: utf-8 -*-

import re


class BrandUtil(object):

    BRAND_BODY = [
        [
            "3.1 Phillip Lim", "MEXX", "JANSPORT", "UNDER ARMOUR", "DONNA KARAN", "JESSICA", "NBA", "Deuter",
            "G2000", "H&M", "Izzue", "Kookai", "LeSportsac", "Nissen", "Thursday Island", "Tough",
            "Uniqlo", "Teenie Weenie", "henri bendel", "la senza", "Lowa", "Zamberlan", "Adele Fado",
            "Denis Simachev", "Lancel", "Valentino", "Bossini", "Versace", "Doc Martins", "Mon Cheri Bridals",
            "A BATHING APE", "Cynthia Rowley", "Edmonton Oilers", "Derek Lam", "Fifa World Cup", "Fifa",
            "Harrods", "Mana", "Ottawa Senators", "Los angeles Lakers", "CHICAGO BULLS", "Minnesota Timberwolves",
            "Miami Heat", "WHY", "Apee", "Friendlies", "Gazelle", "Merrell", "KELLY", "Goldlion",
            "PLAYBOY", "Porter", "Millet", "New York Yankees", "MK MICHAEL KORS", "Body by Jake", "Davidoff", "DC",
            "MORPHSUITS", "Burkini", "Burqini", "Big Show", "HHH", "Kane", "Rey Mysterio", "Alberto Del Rio",
            "Cenation", "Boots To Asses", "Batista", "THE CAMBRIDGE SATCHEL COMPANY", "trunki", "Folli Follie",
            "Nine West", "Camper", "Geox", "Trippen", "Santana day", "Patricia", "10deep", "winnipeg jets", "Aldo",
            "American Tourister", "ASOS", "BCBG Max Azria", "Cerruti 1881", "Buff", "LE PLIAGE", "SHERRI HILL",
            "Chris Jericho", "John Cena", "Shawn Michaels", "Triple H", "Beth Phoenix", "Randy Orton", "Alex Riley",
            "C CHARRIOL", "Roger dubuis", "Catorex", "Edox", "JMG", "Louis Moinet", "Zeno-watch", "Yema",
            "BAUME&MERCIER GENEVE", "Boucheron", "ENZO", "Girard-Perregaux", "Graff", "JOLEE boutique", "MIKIMOTO",
            "Oxette", "Lladro", "G-SHOCK", "Victoria's Secret", "EDIFICE", "PRO TREK", "OCEANUS", "BABY-G", "Enicar",
            "Ernest Borel", "Jaeger", "Orient", "NAUTILUS PATEK PHILIPPE", "Bell&Ross", "Judith Leiber", "Etonic",
            "MOBY", "CAMI SECRET", "J12", "KYMARO", "CELTIC", "ERMENEGILDO ZEGNA", "SUPERDRY", "DAINESE",
            "Galina signature", "VENUM", "Pucci", "FIT FLOP", "FRANKLIN&MARSHALL", "Frey Wille", "boston Celtics",
            "denver Nuggets", "Phoenix Suns", "Portland Blazers", "New Orleans Hornets", "Diane Von Furstenberg",
            "Sacramento Kings", "76ers", "Pacers", "Memphis Grizzlies", "CAMBRIDGE", "Gina", "Dune", "A.Testoni",
            "Bata", "Vasque", "Rock&Republic", "Rugby World Cup", "Sleepy Wrap", "Stackmat",
            "Takeo Kikuchi", "Toronto Maple Leafs", "Tourbillon", "Trikke", "Ufc", "Valdora", "Walkfit", "Lin Shuhao",
            "Washington Capitals", "KIEL JAMES PATRICK", "KJP", "Kikkerland", "A.Lange&Sohne", "Levi Strauss",
            "Levi's", "Levis", "Links", "TROLLBEADS", "Lucky brand", "Stella&Dot", "MCM", "Michael Kors", "Noo",
            "Minnetonka", "Minnetonka Moccasin", "Houston Texans", "Browns", "iheart", "PHILIPP PLEIN",
            "PJS THAT OTHERS MAY LIVE PARAJUMPERS", "PARAJUMPERS", "ic!", "ic", "ic!-berlin", "RW RAYMOND WEIL GENEVE",
            "Red Wing", "RuffleButts", "s.Oliver", "SP La Sposa", "St. Patrick", "DESIGNS BY SHERRI HILL",
            "GIRARD-PERREGAUX", "Body Geometry", "SPIRIT HOODS", "STM", "STRUTZ", "ALUMA WALLET", "BARE LIFTS",
            "WINDSHIELD WONDER", "PERFECT FIT BUTTON", "kimmidoll", "Batchel", "THE CAMBRIDGE SATCHEL BICYCLE",
            "THE NORTH FACE","TNF", "T&CO.", "ICE-WATCH", "Tod's", "Fay", "TOLIX", "JANIE AND JACK", "PROTECTION",
            "ILLUMINATOR", "zigtech", "EAGLE EYES", "MILRY", "XTR", "Stradivarius", "BODE", "AP", "Undertaker",
            "59Fifty", "5950", "7 For All Mankind", "Seven For All Mankind", "New Era", "Casio", "Affliction"
            "A Bathing Ape", "A. Lange&Sohne", "Abercrombie&Fitch", "Adidas", "Adolfo Dominguez", "Adriana Castro",
            "Affliction", "Agnes B", "Air Jordan", "Akademiks", "Akris Punto", "Alberta Ferretti", "Alberto Guardiani",
            "Alejandro Ingelmo", "Alexander McQueen", "Alexander Wang", "Alfred Angelo", "Alice and Olivia", "Alife",
            "Allsaints", "Alpinestars", "Amanda Pearl", "Amaya Arzuaga", "American Eagle", "Andrew GN", "Anlo",
            "Anna Molinari", "Anna Sui", "Anne Klein", "Antik", "Aquascutum", "Arc'teryx", "Armani", "Asics",
            "Audemars Piguet", "AussieBum", "Azzaro", "Azzedine Alaia", "BabyLegs", "BaByliss", "Baby Phat",
            "Balenciaga", "Bally", "Balmain", "Barbour", "Baume et Mercier", "BBC", "Billionaire Boys Club", "BCBG",
            "Bebe", "Bell&Ross", "Belstaff", "Ben Sherman", "Beretta", "Betsey Johnson", "Bijan", "Bikkembergs",
            "Bill Blass", "Billabong", "Birkenstock", "Birkin", "Bjorn Borg", "Blac Label", "Bon Bebe",  "G ",
            "Bottega Veneta", "Bourjois", "Breguet", "Breitling", "Brian Atwood", "Brioni", "Bulova", "Rolex",
            "Burberry", "Bvlgari", "Cacharel", "C1rca", "Callaway", "Calvin Klein", "ck", "Cambrella", "Camelbak",
            "Canada Goose", "Cannondale", "Carachel", "Carmen Marc Valvo", "Carmex", "Carolina Herrera", "Carrera",
            "Cartier", "Casadei", "CAT", "Cath Kidston", "Catherine Malandrino", "Catimini", "Cavalli",
            "Celine", "Champion", "Chanel", "Charles David", "Chaumet", "Cheap Monday", "Chloe", "Chopard",
            "Chris Benz", "Christian Audigier", "Christian Dior", "Christian Lacroix", "Christian Louboutin",
            "Citizen", "Clarks", "Cleveland", "Coach", "Cobra", "Cole Haan", "Colin Stuart", "Collette Dinnigan",
            "Columbia", "Comme Des Garcons", "Concord", "Converse", "Coogi", "Coola Hula Skirt", "Corum", "Creative",
            "Crocs", "Crown Holder", "Dana Buchman", "Daniel Roth", "David Yurman", "New York Knicks", "Dopie",
            "Diesel", "Disney", "Disneyland", "DKNY", "Dolce&Gabbana", "D&G", "Dom Rebel", "Dooney&Bourke",
            "Douglas Hannant", "Dr. Martens", "Dries Van Noten", "DSquared2", "DS", "Duchamp", "Dunhill", "Dunlop",
            "Duvetica", "DVF", "Ebel", "Ecco", "Ecko", "emporio armani", "Ed Hardy", "EFX", "Eley Kishimoto", "Elle",
            "Emilio Pucci", "Energie", "Erickson Beamon", "Escada", "Esprit", "Everlast", "Evis", "Fendi", "Fila",
            "Fitflop", "Fischer", "FjallRaven", "Forever 21", "Fossil", "Fox Head", "Franck Muller", "Franco Moschino",
            "Franklin Marshall", "Fred Leighton", "Fred Perry", "Galliano", "Gant", "GAP", "Gareth Pugh", "Geren Ford",
            "Giambattista Valli", "Gianfranco", "Gianmarco Lorenzi", "Giuseppe Zanotti", "Givenchy", "Monarchy",
            "Glashutte Original", "Golla", "Gore-Tex", "Goyard", "Graeme Black", "Graham", "Grai", "Gray Nicolls",
            "Greedy Genius", "Gretsch", "G-Shock", "G-Star Raw", "Gucci", "Guess", "Hache", "Hackett", "Haglofs",
            "Haider Ackerman", "Hamilton", "Hanae Mori", "Hanii Y", "Harry Winston", "Havaianas", "helena rubinstein",
            "Helmut Lang", "Herve Leger", "Hogan", "Hollister Co", "Hublot", "Hugo Boss", "Hurley", "Ibanez",
            "Ilse Jacobsen", "Insanity", "Irene Galitzine", "iRenew", "Isabel Toledo", "Issa London", "Issey Miyake",
            "IWC", "J. Crew", "Jack Jones", "Jack&Jones", "Jack Wills", "Jack Wolfskin", "Jacob&Co.",
            "Jaeger Lecoultre", "Jason W", "Jawbone", "Jay Godfrey", "Jazzy Toes", "Jean Paul Gaultier", "Jeep",
            "Jemella Ltd", "Jennifer Lopez", "Jessica McClintock", "Jhane Barnes", "Jil Sander", "Jimmy Choo",
            "John Galliano", "Jonathan Saunders", "Judith Ripka", "Juicy Couture", "Juicy", "Junya Watanabe",
            "Kaporal", "Kappa", "Karen Millen", "Karl Lagerfeld", "Kate Spade", "Keen", "Kenneth Cole",
            "Kimora Lee Simmons", "Kipling", "Kitson", "Kobe", "Koi Suwannagate", "Kona", "Kooba", "Ksubi",
            "La Martina", "Le Coq Sportif", "La Mer", "La Prairie", "Lacoste", "Laguna Beach", "Laila Azhar",
            "Lane Bryant", "Lanvin", "Laura Bennett", "Lauren Moffatt", "Lee", "Leg Avenue", "Lela Rose",
            "Leo Schachter", "Lesmills", "Lida Baday", "Lifted Research Group", "LRG", "Links of London",
            "Lisa Perry", "Livestrong", "Liz Claiborne", "Loeffler Randall", "Loewe", "Longchamp", "Longines",
            "Lonsdale", "Louis Vuitton", "LV", "Loro Piana", "Luminox", "Lyle&Scott", "Lyle Scott", "Mad Foot",
            "Maggie Sottero", "Mammut", "Manchester United", "Manolo Blahnik", "Mara Hoffman", "Marc Jacobs",
            "Marchesa", "Mariah Carey", "Mauri", "Max Azria", "Max Mara", "MBT", "Metal Mulisha",
            "Miffy", "Millets", "Miss Sixty", "Miu Mi", "Mizuno", "MLB", "Major League Baseball", "Kenzo Takada",
            "Moncler", "Moon Boot", "Movado", "Mulberry", "Munich", "Nanette Lepore", "New Balance",
            "NFL", "National Football League", "NHL", "Nike", "Nike Shoe", "Nina Ricci", "Nino Cerruti",
            "Nixon", "Nubra", "Nuxe", "Oakley", "Odyssey", "Omega", "Onesies", "Oris", "Oscar De Larenta", "Osiris",
            "Ozark", "P90X", "Paco Chicano", "Paco Rabanne", "Pandora", "Panerai", "Parnis", "Patek Philippe",
            "Paul Frank", "Paul Shark", "Paul Smith", "Peak", "Pegah Anvarian", "Perry Ellis", "Peter Som", "Peuterey",
            "Phiten", "Piaget", "Piazza Sempione", "Pierre Cardin", "Ping", "Police", "Polo Ralph Lauren", "Pony",
            "Porsche Design", "Power Balance", "Prada", "Proenza Schouler", "Pronovias", "Pulsar", "Puma", "Purse Brite",
            "Quiksilver", "Rachel Roy", "Radii", "Rado", "Ralph Lauren", "Ray Ban", "Reebok", "Remo Gianni",
            "Rei Kawakubo", "Replay", "Richard Mille", "Rick Owens", "Rip Curl", "Robert Clergerie", "Roberto Capucci",
            "Robins Jean", "Roca Wear", "Rodarte", "Roger Dubuis", "Romain Jerome",
            "Romero Britto", "Roundtree&Richardson", "Roxy", "Rozae Nichols", "Debbie Meyer",
            "Salvatore Ferragamo", "Samantha Thavasa", "Saress", "Scotch Soda", "Scotty Cameron", "Seamaster",
            "Sean John", "Sebago", "Seiko", "Sergio Rossi", "Shipley&Halmos", "Shipley Halmos", "Silly Bandz",
            "Sinful", "Skechers", "Skip Hop", "Spyder", "Square D", "Stefano Pilati", "Stefano Ricci", "Diadora",
            "Stella McCartney", "Stephen Yearick", "Steve Madden", "Stone Island", "Strenesse", "Stuart Weitzman",
            "Submariner", "Supra", "Supra Footwear", "Supra Tuf", "Swatch", "Swarovski", "Tag Heuer", "Tahari",
            "Takeshy Kurosawa", "Tapout", "Tasco", "Taylormade", "Tech Deck", "Ted Baker", "Temperley", "Terranova",
            "Terra Plana", "Textilene", "Thakoon", "The North Face", "Thierry Mugler", "Thomas Burberry", "Thomas Pink",
            "Thomas Sabo", "Thomas Wylde", "Tiffany&Co.", "Tiffany", "Tiffany Rose", "Timberland", "Timex", "Tissot",
            "Titleist", "Titleist Pro V", "Titoni", "Todd Oldham", "Tokidoki", "Tom Ford", "Tommy Hilfiger",
            "Toms", "Tonino Lamborghini", "Tory Burch", "Tous", "Tower 200", "Toy Watch", "Tracy Reese",
            "Triangle Chalk", "True Religion", "TSE", "Tudor", "Tuleh", "Turbo Jam", "Ubiq", "U-Boat", "UFC", "Ugg",
            "Ulysse Nardin", "Umbro", "Under Armour", "Ungaro", "United Colors of Benetton", "Benetton",
            "Vacheron Constantin", "Valentino Garavani", "Vans", "Vena Cava", "Vera Bradley", "Vera Wang", "Vero Moda",
            "Vibram", "Vince", "Vivienne Westwood", "Vlado", "Volcom", "Volkl",
            "Von Dutch", "Welder", "Wilson", "Wolford", "Wrangler", "Yigal Azroul", "Yohji Yamamoto", "Yonex",
            "Yves Saint Laurent", "Zac Posen", "Zakumi", "Hollister Co.", "Indiana Pacers", "big pony", "chilliwack",
            "Zara", "Zegna", "Zenith", "Abercrombie Fitch", "cristobal balenciaga", "gianfranco ferre", "G-Star",
            "Jack-Wolfskin", "Kenzo", "Oscar De La Renta", "Quicksilver", "emanuel ungaro", "Ysl", "j.crew", "babygap",
            "jypsiere", "ray-ban", "mitchell&ness", "belly bandit", "fuel for life", "jasmin noir", "212 vip",
            "Minnesota Timber Wolves", "THUNDER OKC", "Gymboree", "PROUD TO PLAY", "PROUD TO PLAY IN A NEW ERA",
            "29TWENTY", "39THIRTY", "49FORTY", "F.C.B.", "FCB", "FUTBOL CLUB BARCELONA", "FCBARCELONA", "JABULANI",
            "chrome hearts", "Samsonite", "ic! berlin", "Furla", "Joop!", "VERA WANG PRINCESS", "Blar Label",
            "Lifted Research Group/ Lrg", "Pinko", "JVSLA", "BEAR GRYLLS", "Warriors", "San Antonio Spurs",
            "Massimo Dutti", "dosh", "Glowbys", "Dockers", "Cruciani", "LINDY", "Papa Razzi", "Cruciani People",
            "INSTANT HANDBAG HANGER", "GIORDANO", "fc bayern munchen", "fc bayern", "MOULIN ROUGE", "south africa 2010",
            "Roberto Cavalli", "Allure Bridals", "Alyce", "Bari Jay", "Bonny", "Impression", "Jovani", "Julietta",
            "La Femme", "Mori Lee", "Night Moves", "Sophia Tolli", "Terani Couture", "Voyage", "SLIM CLIP",
            "constellation", "de ville", "PLANET OCEAN", "onitsuka tiger", "chuck taylor", "mercurial", "Airwalk",
            "Mister", "Valleverde", "Hi-Tec", "574", "Tuk", "all star", "blx", "gel kinsei", "vapor", "james",
            "the anti-shoe", "retro 13", "jack purcell", "speedmaster", "le locle", "Van Cleef&Arpels", "lia sophia",
            "nialaya", "chan lu", "PARSIFAL", "Big Bang", "Luminor", "Hermes", "Edge", "Bucks", "Nets", "Creeper Face",
            "BKE", "THE SMURFS", "EASTPAK", "One Million", "rolling stones", "CH"
        ],
        [
            "Acer", "abee", "Geovision", "CISCO", "Zalman", "TRIDENT", "Incipio", "LIFEPROOF", "Adobe", "AKG",
            "Apple", "Asus", "Audio Technica", "Audioquest", "Aura", "Bang&Olufsen", "Beats by Dr. Dre",
            "Benq", "Blackberry", "Bose", "Canon", "Capdase", "Celestica", "Compaq", "Corsair", "Data Traveler",
            "Kingston", "Dell", "Dopod", "DS", "NDS", "NDSL", "Eonon", "EOS", "Epiphone", "Epson",
            "Game Boy Advance", "GBA", "Garmin", "Goldvish", "Hitachi", "HP", "Hewlett Packard", "HTC",
            "IBM", "iLuv", "iMac", "Incase", "Inspiron", "Intuit", "iPad", "iPhone", "iPod", "Jabra", "JBL by Harman",
            "Kenwood", "Spiderpodium Tablet", "MSR606", "Minidx", "TRIPORT", "CM", "Elnec",
            "M in solid circle", "Plantronics", "RAZER", "Cruzer", "SD", "SMS AUDIO", "Play Station", "USBEE", "XPERIA",
            "Klipsch", "Koss", "Lumix", "Mac", "MacBook", "Meizu M8", "Microsoft", "Microsoft Office Live",
            "office ultimate", "Mobiado", "Monster Cable", "monster", "Mophie", "Motorola",
            "MS Access", "MS Exchange Server", "MS SQL Server", "MS Visio", "MS Windows", "Naztech", "Netac", "Nikon",
            "Nintendo", "Nokia", "Olympus", "Otter Box", "Otter", "Palm", "Pioneer", "Playstation", "PS",
            "Pure Acoustics", "Samsung", "Sandisk", "Seidio", "Sennheiser", "Shure", "Skullcandy",
            "Sony Ericsson", "Speck", "Starlogic", "Switcheasy", "Symantec", "Toshiba", "Vaio", "Sony", "Vert",
            "Vinyl Express", "Wii", "Xbox", "Xbox 360", "Zumreed", "Element Case", "HYUNDAI", "Kaspersky", "MYCHARGE",
            "Mighty Dwarf", "LUNATIK", "JumpFromPaper", "Datatraveler", "magic cube usb", "Magicgate", "envy",
            "infinity", "turbine", "jamz", "gumy", "porta pro", "spark plug", "sm58", "mifare", "flash voyager",
            "alienware", "Commuter", "Defender Series", "Jx10 Cara", "Arduino", "GRIFFIN", "MOPHIE JUICE PACK", "oki",
            "bookbook", "Case-Mate", "iRig", "AmpliTube", "GIZMON", "Brother", "Irdeto", "olloclip", "lightning",
            "ISOPROX", "PROXPRO", "PROXPOINT", "PDair", "JUICE PACK PLUS", "HeadCase", "happymori", "beats", "nano",
            "shuffle", "impact series", "reflex series", "ipad 3", "iphone 5", "apple lossless", "PROXCARD",
            "quickbooks", "Visio", "Windows", "norton", "acrobat", "creative suite", "ADOBE ILLUSTRATOR", "photoshop",
            "dreamweaver", "ms exchange client", "anycall", "powershot", "post-it", "QC", "QUIETCOMFORT"
        ],
        [
            "4D Puzzle", "moshi Monsters", "Didicar", "Kaiyodo", "Playwell", "TAKARA", "Troika", "PILLOW PETS",
            "SUNNY PATCH", "Shoulder Buddies", "Zoobles", "BATTLE BRAWLERS", "CRAZY CRITTERS", "KONG", "Sole Skate",
            "FISHER-PRICE", "MONCHHICHI", "Talking Ben", "figurative",
            "Talking Angela", "Air Hogs", "Airzooka", "Angry Birds", "Bakugan", "Barbie", "Bigtime Muscle", "Crazy Cup",
            "Didacar", "Fimo", "Jenga", "Keep A Breast", "LCR", "Magic 8 Ball", "Mattel", "Megatouch", "Moleskine",
            "Mont Blanc", "Nevada Jacks", "Phlat Ball", "Poker Card-Guard", "Power Rangers", "Rubiks' Cube",
            "Shell Shocker", "Speed Stacks", "Stackmat", "Switch Pitch", "Tamagotchi",
            "Transformers", "Transformers Energon", "Transformers the Movie", "Transformers Armada",
            "Universiade 2011", "V-Cube", "Winnie the Pooh", "Lightning McQueen", "Montblanc", "Lego",
            "Air Swimmers", "Talking Tom", "Furby", "DSMX", "litecube", "Lelo", "Magic Cube 10X10X10",
            "Magic Cube 5X5X5", "Magic Cube 6X6X6", "Magic Cube 8X8X8", "Magic Cube 9X9X9", "rubik's", "rubik",
            "Zhuzhu Pets", "magic cube 11x11x11", "magic cube 7x7x7", "MELISSA&DOUG", "Spektrum", "mimicrypet",
            "rubik's cube"
        ],
        [
            "Always", "Fusion", "Gillette", "KOTEX", "KLEENEX", "HUGGIES", "Speed Stick", "Wish",
            "Crabtree&Evelyn", "Clarisonic Opal", "ROSEBUD", "RSS", "HEELTASTIC", "Huggies", "Mach 3",
            "Moon Cup", "Pampers", "DHC", "LiLash"
        ],
        [
            "NOGUCHI", "Mobiseat", "Magic Bullet", "Magic Bullet Express", "GERBER", "Fatboy", "Penetrator",
            "TWIN DRAFT GUARD", "LUMATEK", "DREAM LITES", "SLUSHY MAGIC", "XHOSE", "TEMPUR", "kohler",
            "Bullet Blender", "Bullet Juicer", "MUL-T-LOCK", "9 Minute Marinator", "Aqua Globes", "Baxter",
            "PROVASI", "SOHER", "Dornbracht", "LION", "Pigeon", "GYRO BOWL",
            "FLOS", "Table-Mate", "West Elm", "Wisdom", "Touch clean", "Z-BAR", "CLEAN STEP MAT", "LONGOSTAND",
            "LINT LIZARD", "TERVIS", "TERVIS TUMBLER", "Clipa", "VAPUR", "THE ANTI-BOTTLE", "waterpik", "Ashburn",
            "Bake 'N Fill", "Bar Butler", "Brababy", "Braball", "Bra Ball", "Celluless", "Duracell", "ERGObaby",
            "Eveready", "Forearm Forklift", "Furminator", "Grill Daddy", "H2O Mop", "Jacuzzi", "Kosmodisk",
            "Levitron", "Lladro", "Lock Back", "Miracle Blade", "Oral-B", "Palmscale", "Pantree", "Ped Egg",
            "Sleepy Wrap", "Son of Hibachi", "Talking Toilet Paper", "Total Trolley", "Totseat", "Tupperware",
            "Victorinox", "Walk Fit", "Walkfit", "Zippo"
        ],
        [
            "Benefit", "Avene", "Bioderma", "Biore", "Boots BOTANICS THE POWER OF PLANTS", "Borghese", "Albion",
            "HSI PROFESSIONAL", "TRESEMME", "Valmont", "soap&Glory", "pantene", "Gaultier", "Paco Rabanne",
            "Camenae", "Carmex", "Caudalie", "Coppertone", "Dr.Ci:Labo", "Dr.Hauschka", "Etude", "Evian", "Fancl",
            "Fruit of the Earth", "JUJU", "Kanebo", "KAO", "L'occitane fresh skincare", "La colline", "LANEIGE", "Lush",
            "Make up for ever", "Origins", "Revlon", "RMK GEL SCRUB", "Uriage", "Vichy", "VOV", "Weleda", "Za",
            "Cetaphil", "Decleor", "Burt's Bees", "OMNIA", "Orofluido", "Love and Glamour JENNIFER LOPEZ", "Deseo",
            "J.LO", "Kiehl's", "Daisy Marc Jacobs", "ECO TOOLS", "BEAUTYBLENDER", "PINK", "EZ COMBS",
            "EOS EVOLUTION OF SMOOTH", "EOS The Evolution of Smooth", "Evolution of Smooth", "VASELINE", "Dove",
            "Violent Lips", "Echo", "i.d. bareMinerals", "LV LOUIS VICTORIA", "Biotherm", "Bobbi Brown",
            "Clarins", "Clinique", "Coco", "Chanel", "Elizabeth Arden", "Endermologie", "Endermology", "Endermologia",
            "Estee Lauder", "Guerlain", "H2o", "Hydrolyze", "J'adore", "Dior", "Jurlique", "Kose", "Lancome",
            "L'Oreal", "MAC", "Make Up Forever", "Max Factor", "Maybelline", "Nars", "O P I", "Olay", "Paris Hilton",
            "Poison", "Hypnotic Poison", "Midnight Poison", "Pure Poison",
            "Schwarzkopf", "T3", "Sephora", "Shiseido", "Shu Uemura", "Sisley", "SK-II", "Skin79", "Smashbox",
            "St. Dupont", "Sunkist", "Too Faced Cosmetics", "Viva Glam", "Yves Rocher", "Intenze", "Farouk",
            "Magic Leverag", "Gelish", "urban decay", "urban decay naked", "EUPHORIA", "COOL WATER", "CURLFORMERS",
            "Slique", "Cheyenne", "TWEEZ'E", "EMJOI", "Baby Banana", "LIVE JENNIFER LOPEZ", "MICKY SHARPZ",
            "YSL MONOGRAM", "Opi", "Too Faced", "laroche posay", "hr", "hypnotic poison",
            "pure poison", "Tendre Poison", "poison", "arpege", "attitude extreme", "bad gal", "benetint",
            "blanc expert", "dr.feelgood", "erase paste", "high beam", "lola", "NUTRIX ROYAL", "only the brave",
            "PHOTOGENIC LUMESSENCE", "plushglass", "sed", "studio sculpt", "thrrrob", "tresor", "tropiques",
            "you rebel", "zoom lash", "dazzleglass", "clarisonic", "No5", "One Million", "DHC"
        ],
        [
            "SHOES UNDER", "Tetra Pak", "KAPTON", "Dicota", "BOXWAVE", "KEYBOARD BUDDY", "Spiderpodium Tablet",
            "Breffo", "Beer Savers", "Dexion", "FRESHFIBER", "INOX CASE", "KATE SPADE NEW YORK", "Spider podium",
            "LONGOPAC", "PAXXO", "POWER PRO", "OVI", "Candyshell", "BOTTLE TOP", "XEROX", "X-design", "Acase",
            "Lighter Leash", "Thom Browne"
        ],
        [
            "APexi", "Advanced Elements", "Odyssey", "b'twin", "Panamera", "MA AUDIO",
            "Valdora", "Wheelman", "General Motors", "Tarmac", "s works", "strida", "Auto Meter", "Blata",
            "Blitz", "BMW", "Ducati", "Ferrari", "Go-Ped", "GReddy", "Harley Davidson", "HKS", "Honda", "bosch"
            "Polaris", "Segway", "Shimano", "Skyteam", "Sky Team", "Takata", "Trikke",
            "Yamaha", "FSA", "Scott", "LAND ROVER", "Audi", "Auto Com", "car-freshner",
            "Porsche", "brabus", "mongoose", "HAMANN", "Skunk2", "A2B", "RIGID INDUSTRIES", "Federal", "Acura"
        ],
        [
            "Air Multiplier", "Andis", "Baby Bullet", "Vita-mix", "Braun", "ENELOOP", "Delonghi", "Mte",
            "ENERGIZER", "Fissler", "Honeywell", "Kosmodisk", "Radio shack", "Senseo", "Square D", "STICK N CLICK",
            "Disco Panel", "Might Morphin Power Rangers", "OCTO", "STICK UP BULB", "GO DUSTER", "PASTA N MORE", "Vizio"
            "H2O MOP", "Venus", "X-MINI", "BOWERS&WILKINS", "Bosch HID", "CHI", "Dirt Devil", "Dreambox", "DStv",
            "Dyson", "GHD", "Go Duster", "Instyler", "Ionspa Footbath", "JVC", "LG", "Life Ionizer", "Mitsubishi",
            "MTE", "NEC", "Panasonic", "Philips", "RadioShack", "Sharp", "Siemens", "Sonic Scrubber", "Spin Spa",
            "Split Ender", "Stick-Up Bulb", "Swivel Sweeper", "The Magic Bullet", "Vita-Mix", "DRYER MAX", "JOVEN"
        ]
    ]

    @classmethod
    def check_brand_at_title(cls, title):
        title = title.lower()
        for brand_group in cls.BRAND_BODY:
            for brand in brand_group:
                for nb in cls.transform_brand(brand):
                    if nb in cls.transform_title(title):
                        return brand
        return False

    @classmethod
    def transform_title(cls, title):
        title = re.sub(" {2,}", " ", title)
        title = re.sub("-+", " ", title)
        title = re.sub(" *& *", "&", title)
        return " " + title + " "

    @classmethod
    def transform_brand(cls, brand):
        if len(brand) < 5:
            return [" " + brand + " "]
        brand = brand.lower()
        brand_list = list()
        brand_list.append(brand)
        if " " in brand:
            brand_list.append(brand.replace(" ", "-"))
        if "-" in brand:
            brand_list.append(brand.replace("-", " "))
        if "'" in brand:
            brand_list.append(brand.replace("'", ""))
        return brand_list

    @classmethod
    def check_brand(cls, title):
        return cls.check_brand_at_title(title)
