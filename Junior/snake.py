def snakefill(side):
    area = side*side
    snake_bites = 0
    snake_size = 1

    found = False
    while found == False:
        if snake_size * 2 <= area:
            snake_bites += 1
            snake_size *= 2
        else:
            found = True
    
    return snake_bites
        

