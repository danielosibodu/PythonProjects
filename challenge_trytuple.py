albums = [["Welcome to my Nightmare", "Alice Cooper", 1975, 
         (
            (1,"Pulling the rugs"),
            (2, "Psycho"),
            (3, "Mayhem"), 
            (4,"Run it down")
            )],
         ["Bad Company", "Bad Company", 1974,
         (
            (1,"Radioactive"),
            (2, "rino"),
            (3, "believer"), 
            (4,"Run it once")
            )],
         ["Nightflight", "Budgie", 1981,
         (
            (1,"Pulling the rugs"),
            (2, "Psycho"),
            (3, "Mayhem"), 
            (4,"Run it down")
            )],
         ["More Mayhem", "Emilda May", 2011,
         (
            (1,"Pulling the rugs"),
            (2, "Psycho"),
            (3, "Mayhem"), 
            (4,"Run it down")
            )]],
for album in albums:
    for alb in album:
        print("Album: {0}     Artist: {1}     Year: {2}     Song: {3}"
        .format(alb[0],alb[1],alb[2],alb[3]))
    # album,artist,year,song = 
    
    