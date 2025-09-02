from collections import deque
import sys


data = sys.stdin.read()
lines = data.splitlines()

rows = int(lines[0])
columns = int(lines[1])
up_to = int(lines[2])

# edge-case no rows
if rows == 0 or columns == 0:
    print(0)
    sys.exit()


q = deque()
# Starting Row - cost, row, col
for col in range(columns):
    q.append((((col % up_to) + 1), 0, col))


lowest_cost = 10000000000000    # Big ahh value - my makeshift inf.
while q:
    cost, row, col = q.popleft()

    # reached other side
    if row == (rows - 1):
        lowest_cost = min(lowest_cost, cost)

    else:
        for choice in [-1, 0, 1]:
            next_col = col + choice

            # Make sure its in bounds
            if 0 <= next_col < columns:
                new_cost = cost + ((((row + 1) * columns + next_col) % up_to) + 1)
                q.append((new_cost, row + 1, next_col))

print(lowest_cost)



