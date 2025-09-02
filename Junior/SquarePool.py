import sys

data = sys.stdin.read()
lines = data.splitlines()

side_length = int(lines[0])
trees = int(lines[1]) 

# pool setup: * = clear space and T = tree space.
square = ["*"] * side_length
for i in range(side_length):
    square[i] = ["*"] * side_length

for i in range(trees):
    row, column = map(int, lines[i+2].split())
    square[row-1][column-1] = "T"

# possible square check
def possible_square(square_side_length, amount_squares, amount_before_move_down):
    counter = 0
    column_starter = -1
    for i in range(amount_squares):
        column_starter += 1    # starts at zero
        if (i % amount_before_move_down) == 0 and i != 0:
            counter += 1
            column_starter = 0    # when you move down row, start back again at 0
        
        # Check if any tree is in the current row range; need to fix
        for j in range(square_side_length):
            if "T" in set((square[(counter + j)][column_starter:(square_side_length + column_starter)])):
                break
            elif j == (square_side_length - 1):
                return True
    return False


for i in range(side_length):
    square_check = side_length - i
    if possible_square(square_check, (side_length - square_check + 1) ** 2, (side_length - square_check + 1)) == True:
       print(square_check)
       break
       
       
       






