shopping_lists= ["milk",
                 "milo",
                 "flakes",
                 "oats",
                 "detergents"
                ]
another_list = shopping_lists
print(id(another_list))
print(id(shopping_lists))

shopping_lists+=["cookies"]
print(shopping_lists)
print(id(shopping_lists))                           
print(another_list)#cookies will be added to shopping_lists
print()
a = b = c = d = e = f =shopping_lists # they all have the values of shopping_lists
print("adding cream")
b.append("cream")
print(a) # since a,b,c,d,e,f are same