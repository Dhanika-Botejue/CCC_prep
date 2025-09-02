import sys

data = sys.stdin.read()
lines = data.splitlines()

amount = int(lines[0])
# creating sunflowers multi-dimensional list
sunflowers = [None] * amount
for i in range(amount):
    sunflowers[i] = [None] * amount
# mapping values
for i in range(amount):
    for j in range(amount):
        sunflowers[i][j] = int(lines[i+1].split(" ")[j])

# check if meets requirements to be data
def check_list():
    for i in range(amount):
        for j in range(amount):
            # conditions
            if sunflowers[i] != sorted(sunflowers[i]):
                return False
            if i < (amount-1):
                if (sunflowers[i][j] < sunflowers[i+1][j]) == False:
                    return False
            if i == (amount - 1) and j == (amount - 1):
                for k in range(amount):
                    print(*sunflowers[k], sep = " ") # cool thing i learned to print elements of list

# check if the table wasn't rotated
check_list()

store_values = [None] * amount
for i in range(amount):
    store_values[i] = [None] * amount

# three rotations to do
for i in range(3):
    # reset
    for j in range(amount):
        for k in range(amount):
            store_values[j][k] = sunflowers[j][k] # reset
    
    # do rotation and update sunflowers
    for j in range(amount):
        for k in range(amount):
            sunflowers[j][k] = store_values[amount-1-k][j]

    # check if it is valid data 
    check_list()









            

        


