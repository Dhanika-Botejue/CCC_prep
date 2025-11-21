import sys

data = sys.stdin.read()
lines = data.splitlines()

rows = int(lines[0])
columns = int(lines[1])

def farmer_row_value(columns, farmer_row, farmer_column):
    row_total = 0
    row_total += pumpkin_values[patch[farmer_row][farmer_column]] 

    # going right
    for i in range(columns):
        if farmer_column+i+1 < columns and patch[farmer_row][farmer_column+i+1] != "*":
            row_total += pumpkin_values[patch[farmer_row][farmer_column+i+1]]
        else:
            break
       
    # going left
    for i in range(columns):
        if farmer_column-i-1 >= 0 and patch[farmer_row][farmer_column-i-1] != "*":
            row_total += pumpkin_values[patch[farmer_row][farmer_column-i-1]]
        else:
            break
    return row_total


total = 0
# cost of pumpkins
pumpkin_values = {"S" : 1 , "M" : 5, "L" : 10}

# creating multi dimensional array (patch)
patch = [None] * rows

for i in range(rows):   
    patch[i] = [None] * columns

# assigning values in patch
for i in range(rows):
    for j in range(columns):
        patch[i][j] = lines[i+2][j]

# farmer position
farmer_row = int(lines[rows+2])
farmer_column = int(lines[rows+3])  

# cost of pumpkin that farmer is immidiately at
#total += pumpkin_values[patch[farmer_row][farmer_column]]
#patch[farmer_row][farmer_column] = "F"


total += farmer_row_value(columns, farmer_row, farmer_column)

# going up
for i in range(rows):
    for j in range(columns):
        if patch[farmer_row-1][farmer_column] != "*" and farmer_row-1 >= 0:
            farmer_row -= 1
            total += farmer_row_value(columns, farmer_row, farmer_column)
            break
# going down
for i in range(rows):
    for j in range(columns):
        if farmer_row+1 < rows and patch[farmer_row+1][farmer_column] != "*":
            farmer_row += 1
            total += farmer_row_value(columns, farmer_row, farmer_column)
            break

#for i in range(rows):
#   print(patch[i])

print(total)

