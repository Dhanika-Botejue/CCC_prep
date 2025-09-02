import sys

data = sys.stdin.read()
lines = data.splitlines()

small_treats = int(lines[0])
medium_treats = int(lines[1])
large_treats = int(lines[2])

happiness = small_treats * 1 + medium_treats * 2 + large_treats * 3

if happiness >= 10:
    print("happy")
else:
    print("sad")
