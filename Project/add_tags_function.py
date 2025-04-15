import json
from view_tags_function import tags

def add_tags(tag_map):
    
#allows to add new category to tag_map and prevents addition of a duplicate category
    ask = input("Enter the name of new category: ").lower().strip()
    if ask in tag_map:
        print('\033[1;31m' + f"Category {ask} already exists. Go to update_tags_function." + '\033[0m')
        return tag_map
    else:
        
        print('\033[1;32m' + f"Let's Add Tags to this {ask}" . upper() + '\033[0m')

        print('\033[1;32m' + "Note : Flat category means there are no sub_categries to tags. Its a single dict required"  + '\033[0m' )
        print('\033[1;32m' + "Note : Nested category means there are subcategories to tags. Its a dict of dict required" + '\033[0m')

        tag_structure = input(f"Is the {ask} category flat or nested? (flat/nested): ").lower().strip()
        if tag_structure == "flat":
            tags = input(f"Enter the tags for {ask} category (comma-separated): ").lower().split(",")
            tags = [tag.strip() for tag in tags]
            tag_map[ask] = tags
          
        elif tag_structure == "nested":
            tag_map[ask] = {}
            while True:
                sub_key = input(f"Enter a subcategory for {ask} (or type 'done' to finish): ").lower().strip()
                if sub_key == "done":
                    break
                sub_tags = input(f"Enter the tags for the {sub_key} subcategory (comma-separated): ").lower().split(",")
                sub_tags = [tag.strip() for tag in sub_tags]
                tag_map[ask][sub_key] = sub_tags
              
        print('\033[1;32m' + f"New category {ask} added" + '\033[0m')

        with  open("tag_map.json", "w") as file:
            json.dump(tag_map, file, indent=4)
   
    return tag_map




        
        