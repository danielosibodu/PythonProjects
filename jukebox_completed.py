from nested_dataa import albums 
SONG_LISTS_INDEX= 3 # constants are written with capital letter

while True:
    print("please choose your album (invalid choice exists)")
    for index,(title, artist, year, song) in enumerate(albums):
        print("{} {}. "
        .format(index + 1, title))
    choice = int(input())
    if 1 <= choice <= len(albums):
        song_lists = albums[choice - 1][SONG_LISTS_INDEX] # same as using [3] because song list is in index position 3    
    else:
        break
    print("Enter the song number")
    for index, (track_number,song) in enumerate(song_lists):
        print("{}: {}".format(index +1,song))    
    select = int(input())
    if 1 <= select <= len(song_lists):
        print("{} playing".format(song))
        
    print("="*50)


    # print(albums[choice - 1])