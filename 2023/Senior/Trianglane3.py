import sys

data = sys.stdin.read()
lines = data.splitlines()

length = int(lines[0])
row_1 = lines[1].split()
row_2 = lines[2].split()

total = 0

prev_seen1 = False
prev_seen2 = False

for i in range(length):
    cur_1 = int(row_1[i])
    cur_2 = int(row_2[i])

    # row 1
    if cur_1 == 0:
        prev_seen1 = False
    else:
        # adjacent case
        if prev_seen1 == True:
            total += 1
        # new triangle without any adjacents
        else:
            prev_seen1 = True
            total += 3
    
    # row 2
    if cur_2 == 0:
        prev_seen2 = False
    else:
        # adjacent case
        if prev_seen2 == True:
            total += 1
        # new triangle without any adjacents
        else:
            prev_seen2 = True
            total += 3
    
    # bases are shared by painted triangles on even (index-zero) triangles
    if cur_1 == 1 and cur_2 == 1 and (i % 2 == 0):
        total -= 2


print(total)




# idea
#compute top row - when first triangle seen add 3, any consecutives add 1. if none seen before another seen add 3 again
#then, same for bottom row. 
#if both bottom and top are black trianle in a column, the reduce two from total