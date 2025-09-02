import sys

data = sys.stdin.read()
lines = data.splitlines()

games = [lines[0], lines[1], lines[2], lines[3], lines[4], lines[5]]

count = 0
for i in range(6):
    if games[i] == "W":
        count += 1

if count > 4:
    print(1)
elif count > 2:
    print(2)
elif count > 0:
    print(3)
else:
    print(-1)