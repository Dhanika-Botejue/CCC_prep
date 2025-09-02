import sys

data = sys.stdin.read()
lines = data.splitlines()

columns = int(lines[0])

tape_length = 0
row_1 = lines[1].split()
row_2 = lines[2].split()

triangles_in_a_row1 = False
triangles_in_a_row2 = False 

for i in range(columns):
    # row 1
    if row_1[i] == "1" and triangles_in_a_row1 == False:
        tape_length += 3
        triangles_in_a_row1 = True
    elif row_1[i] == "1" and triangles_in_a_row1 == True:
        tape_length += 1
    elif row_1[i] == "0":
        triangles_in_a_row1 = False
    # row 2
    if row_2[i] == "1" and triangles_in_a_row2 == False:
        tape_length += 3
        triangles_in_a_row2 = True
    elif row_2[i] == "1" and triangles_in_a_row2 == True:
        tape_length += 1
    elif row_2[i] == "0":
        triangles_in_a_row2 = False
    # remove middle lines
    if row_1[i] == "1" and row_2[i] == "1" and (i % 2) == 0:
        tape_length -= 2    # subtract two because there is one piece on each side and when combined is none

print(tape_length)