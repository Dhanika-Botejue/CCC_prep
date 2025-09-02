import sys

# Read all input at once
data = sys.stdin.read()

# Split the input into separate lines
lines = data.splitlines()

# Extract the number of plates from the lines
red = int(lines[0])  # First line
green = int(lines[1])  # Second line
blue = int(lines[2])  # Third line

# Calculate the total cost
total_cost = red * 3 + green * 4 + blue * 5

# Print the total cost
print(total_cost)



"""
red = int(input())
green = int(input())
blue = int(input())
print(red * 3 + green * 4 + blue * 5)
"""
