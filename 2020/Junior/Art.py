import sys

data = sys.stdin.read()
lines = data.splitlines()

paint_drops = int(lines[0])

# setup for the loop
smallest_x = int((lines[1].split(","))[0])
biggest_x = 0

smallest_y = int((lines[1].split(","))[1])
biggest_y = 0

for i in range(paint_drops):
    x = int((lines[i+1].split(","))[0])
    y = int((lines[i+1].split(","))[1])
    
    if x < smallest_x:
        smallest_x = x
    if x > biggest_x:
        biggest_x = x
    if y < smallest_y:
        smallest_y = y
    if y > biggest_y:
        biggest_y = y

smallest_x -= 1
smallest_y -= 1
biggest_x += 1
biggest_y += 1

print(f"{smallest_x},{smallest_y}")
print(f"{biggest_x},{biggest_y}")

