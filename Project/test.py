from view_tags_function  import tags
from add_tags_function import add_tags
from add_producer_function import add_producers
from tag_to_producer import find_category_tags

tag_map = tags()
add_tag = add_tags(tag_map)
producers = add_producers()
cat_tag = find_category_tags(tag_map, producers, "producer_2")



