import sys

data = sys.stdin.read()
lines = data.splitlines()

rows = int(lines[0])
columns = int(lines[1])

cells = [None] * rows
for i in range(rows):
    cells[i] = [None] * columns

for i in range(rows):
    for j in range(columns):
        cells[i][j] = int((lines[i+2].split(" "))[j])

print(cells)