from add_producer_function import add_producers
from view_tags_function import tags

#assigning category_tags and tags to producer_service

def find_category_tags(tag_map,service,producer_name):
    input = input(f"Enter {producer_name} to append tag to ").split(",")
    if input not in producer_name:
        print("Please enter a valid producer name")
    else:
        category_tags= []
        for category, tags in tag_map.items():
            if service in category:
                return category


           

