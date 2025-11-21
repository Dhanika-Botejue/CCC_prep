import sys

data = sys.stdin.read()
lines = data.splitlines()

rows = int(lines[0])
columns = int(lines[1])

total = 0
# cost of pumpkins
pumpkin_values = {"S" : 1 , "M" : 5, "L" : 10, "*" : 0}

# creating multi dimensional array (patch)
patch = [None] * rows

for i in range(rows):   
    patch[i] = [None] * columns

# gave up so instead ill take the one point; better than none
for i in range(rows):
    for j in range(columns):
        total += pumpkin_values[lines[i+2][j]]

print(total)

