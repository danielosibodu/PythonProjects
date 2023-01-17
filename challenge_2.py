# print("Please choose your option in the list below")
# print("1\tBeans")
# print("2\tRice")
# print("3\tEggs")
# print("4\tChicken")
# print("5\tSoup")
# print("6\tSpagg")
# print("0\tExit")
option= "-"
# while True:
    
#     if option == "0":
#         break
#     elif option in "123456":
#         print("Good we'll add {} to cart".format(option))
#     else: 
#         print("Please choose your option in the list below")
#         print("1:\tBeans")
#         print("2:\tRice")
#         print("3:\tEggs")    
#         print("4:\tChicken")
#         print("5:\tSoup")
#         print("6:\tSpagg")
#         print("0:\tExit")
 
#     option= input("CHose one o")
#or
while option != "0":
    if option in "123456":
        print("Good we'll add {} to cart".format(option))
    else: 
        print("Please choose your option in the list below")
        print("1:\tBeans")
        print("2:\tRice")
        print("3:\tEggs")    
        print("4:\tChicken")
        print("5:\tSoup")
        print("6:\tSpagg")
        print("0:\tExit")
 
    option= input("CHose one o")