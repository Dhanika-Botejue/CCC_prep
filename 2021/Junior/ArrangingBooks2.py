import sys

data = sys.stdin.read().strip()
amount = len(data)

# Count occurrences of 'L' and 'S'
num_L = data.count('L')
num_S = amount - num_L  # Since only 'L' and 'S' exist

# Count misplaced 'L' in the S-region
misplaced_L = 0
for i in range(num_L):
    if data[i] == 'S':
        misplaced_L += 1

# Count misplaced 'S' in the L-region
misplaced_S = 0
for i in range(num_L, amount):
    if data[i] == 'L':
        misplaced_S += 1

# The swaps needed is the number of misplaced pairs that need to be swapped
min_swaps = min(misplaced_L, misplaced_S)
print(min_swaps)