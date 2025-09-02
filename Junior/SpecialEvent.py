import sys

data = sys.stdin.read()
lines = data.splitlines()

days = [0, 0, 0, 0, 0]

people = int(lines[0])

for i in range(people):
    for j in range(5):
        if lines[i+1][j] == "Y":
            days[j] += 1

highest = []
highest_amount = 0

for i in range(5):
    if days[i] > highest_amount:
        highest_amount = days[i]

for i in range(5):
    if days[i] == highest_amount:
        highest.append(i+1)

# makes highest list all into string, then join can put commas between values
print((",").join(map(str, highest)))    