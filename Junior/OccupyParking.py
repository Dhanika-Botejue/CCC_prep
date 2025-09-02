import sys

data = sys.stdin.read()
lines = data.splitlines()

spots = int(lines[0])
day_1 = []
day_2 = []

for i in range(spots):
    day_1.append(lines[1][i])
    day_2.append(lines[2][i])


count = 0
for i in range(spots):
    if day_1[i] == "C" and day_2[i] == "C":
        count += 1

print(count)