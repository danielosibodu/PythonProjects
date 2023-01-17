shopping_lists= ["milk","milo","flakes","oats","detergents"]
# for item in shopping_lists:
#     if item != "detergents":
#         print("buy "+item)



# for item in shopping_lists:
#     if item == "detergents":
#         continue
#     print("buy "+item)


for item in shopping_lists:
    if item == "flakes":#it will stop at milo
        break
    print("buy "+item)

