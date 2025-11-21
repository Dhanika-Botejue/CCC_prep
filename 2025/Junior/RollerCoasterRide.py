import sys

data = sys.stdin.read()
lines = data.splitlines()

position = int(lines[0])
total = (int(lines[1]) * int(lines[2]))

if position > total:
    print("no")
else:
    print("yes")
