import sys

data = sys.stdin.read()
lines = data.splitlines()

donuts = int(lines[0])
events = int(lines[1])

total_more_lines = events * 2

action = ""
for i in range(total_more_lines):
    if i % 2 == 0:
        action = lines[i+2]
    else:
        if action == "+":
            donuts += int(lines[i+2])
        elif action == "-":
            donuts -= int(lines[i+2])

print(donuts)