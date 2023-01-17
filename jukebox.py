from nested_dataa import albums 

while True:
    print("please choose your album (invalid choice exists)")
    for index,(title, artist, year, song) in enumerate(albums):
        print("{} {} {} {}"
        .format(index + 1, artist, year, song))

    # for index,value in enumerate(albums):
    #     title, artist, year, song = value
    #     print(index + 1,value)
