import sys

data = sys.stdin.read()
lines = data.splitlines()

rows = int(lines[0])
columns = int(lines[1])

patch = [None] * rows
for i in range(rows):
    patch[i] = [None] * columns

for i in range(rows):
    for j in range(columns):
        patch[i][j] = lines[i+2][j]

farmer_row = int(lines[2+rows])
farmer_column = int(lines[3+rows])

def harvest_dfs(r, c, patch, visited):
    # Base cases: Out of bounds, hay bale, or already visited
    if r < 0 or r >= len(patch) or c < 0 or c >= len(patch[0]) or patch[r][c] == '*' or (r, c) in visited:
        return 0

    # Value mapping for pumpkins
    pumpkin_values = {'S': 1, 'M': 5, 'L': 10}

    # Mark as visited
    visited.add((r, c))

    # Harvest current pumpkin if applicable
    total_value = pumpkin_values.get(patch[r][c], 0)

    # Recursive DFS in all four directions
    total_value += harvest_dfs(r - 1, c, patch, visited)  # Up
    total_value += harvest_dfs(r + 1, c, patch, visited)  # Down
    total_value += harvest_dfs(r, c - 1, patch, visited)  # Left
    total_value += harvest_dfs(r, c + 1, patch, visited)  # Right

    return total_value

visited = set()
result = harvest_dfs(farmer_row, farmer_column, patch, visited)
print(result)