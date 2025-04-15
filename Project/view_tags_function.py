import json
import os

def tags():
 #to save and define tag_map so as to allow for updates
    if not os.path.exists("tag_map.json"):
        with open("tag_map.json", "w") as file:
            json.dump({}, file)

    with open("tag_map.json", "r") as file:
        tag_map = json.load(file)

    hardcoded_tag_map = {
    # Hair Services
        "hair": [
            "beauty", "haircare", "styling", "salon", "naturalhair", 
            "cornrows", "protectivestyles"
        ],
        "afrohair": [
            "afro", "naturalhair", "blackbeauty", "protectivestyles", "treatments"
        ],
        "haircut": [
            "men_haircut", "barbing", "hairstyles", "female_haircut", "hairtrends"
        ],
        "braids": {
            "styles": [
                "boxbraids", "knotless", "ghanaweaving", "cornrows", 
                "fulanibraids", "lemonadebraids", "butterflybraids", "twists"
            ],
            "lengths": [
                "short", "medium", "long"
            ],
            "specifics": [
                "microbraids", "mediumbraids", "longbraids", "braidslength_short",
                "braidslength_medium", "braidslength_long"
            ]
        },
        "crotchet": {
            "styles": [
                "crochetbraids", "fauxlocs", "springtwist", "boholocs", "waterwave"
            ],
            "lengths": [
                "short", "medium", "long"
            ]
        },
        "locs": [
            "fauxlocs", "microlocs", "sisterlocks", "interlocks", "starterlocs",
            "retwist", "freeformlocs", "highlocs", "lowlocs"
        ],
        "wigs": [
            "wiginstallation", "wigrevamping", "wigfixin", "wigstyling", "wigcare",
            "lacewigs", "closurewigs", "frontalwigs", "humanhairwigs", "syntheticwigs", 
            "customwigs", "wigrepair", "wigcleaning", "wigtrimming", "hairreplacement"
        ],

        # Beauty Services
        "makeupartist": [
            "beauty", "makeup", "mua", "cosmetics", "makeupartist", 
            "weddingmakeup", "birthdaymakeup", "glam", "photoshoot", "eventmakeup"
        ],
        "makeup": [
            "beauty", "cosmetics", "mua", "glam"
        ],
        "nails": [
            "beauty", "nailart", "manicure", "pedicure", "acrylicnails", "gelnails"
        ],
        "skincare": [
            "beauty", "skincare", "glow", "wellness", "facials", "organicproducts"
        ],

        # Food & Catering
        "afrodishes": [
            "food", "africanfood", "afrodishes", "traditional", "nigerianfood", 
            "ghanianfood", "eventcatering", "deliveries"
        ],
        "afrocuisines": [
            "africanfood", "recipes", "cuisine", "spices", "jollof", "ofada", 
            "fried", "fufu", "soup"
        ],
        "cakes": [
            "desserts", "baking", "cakes", "celebration", "customcakes", 
            "birthdays", "weddings", "eventcakes"
        ],
        "pastries": [
            "desserts", "snacks", "bakedgoods", "pastries", "meatpie", 
            "puffpuff", "chinchin"
        ],
        "snacks": [
            "snacks", "meatpie", "doughnut", "glazeddoughnut", "milkydoughnut", 
            "chinchin", "sausage", "eggroll", "stickmeat", "smallchops", "puffpuff"
        ],

        # Retail & African Shops
        "africanshops": [
            "africanmarket", "culture", "grocery", "africanproducts", "retail",
            "hairproducts", "spices", "fabrics", "ankara", "africanfashion", "accessories"
        ],

        # Features & Special Services
        "features": [
            "homeservice", "kidsfriendly", "inhomesalon", "mobilebusiness",
            "femaleonly", "walkin", "byappointment"
        ],

        # Event Services
        "eventservices": [
            "eventcatering", "deliveries", "buffet", "outdoorcatering", 
            "smallchops", "eventplanning"
        ]
    } 
      #to add list of hardcoded tags to the tag_map
    tag_map.update(hardcoded_tag_map)


    for category,tags in tag_map.items():
        print('\033[1;32m' + f"\n {category.capitalize()}:"+ '\033[0m')
        if isinstance(tags,dict):
            for sub_key, sub_tags in tags.items():
                print(f"   {sub_key.capitalize()}:" )
                for tag in sub_tags:
                    print('\033[1;37m'+ f"     {tag}" + '\033[0m')
        else:
            for tag in tags:
                print('\033[1;37m' + f"   {tag}" + '\033[0m')
   

    return tag_map
