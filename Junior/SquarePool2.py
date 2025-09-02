import sys

data = sys.stdin.read()
lines = data.splitlines()

side_length = int(lines[0])
trees = int(lines[1])
tree_row, tree_column = lines[2].split(" ")

tree_row = int(tree_row)
tree_column = int(tree_column)

square = [None] * side_length
for i in range(side_length):
    square[i] = [None] * side_length