import sys

data = sys.stdin.read()
lines = data.splitlines()

people = int(lines[0])
highest_bid = 0

for i in range(people*2):
    if ((i+1) % 2 == 0):
        if int(lines[i+1]) > highest_bid:
            highest_bid = int(lines[i+1])
            person = lines[i]

print(person)
