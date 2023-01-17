shopping_lists= ["milk","milo","flakes","oats","detergents"]
item_to_find="flakes"
found_at= None
# for i in range(len(shopping_lists)):#if we dont use len function    for i in range(6)
#     if item_to_find == shopping_lists[i]:
#         found_at=i
#         break
# if found_at is not None:
#     print("Item found at {}".format(found_at))
# else:
#     print("item not found")
if item_to_find in shopping_lists:
    found_at= shopping_lists.index(item_to_find)
    print("the item found at {}".format(found_at))
else:
    print("Not found")