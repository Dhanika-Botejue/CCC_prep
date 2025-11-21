import sys

data = sys.stdin.read()
lines = data.splitlines()

year = int(lines[0])

while True:
    year += 1
    year_digits_set = set(list(str(year)))
    if len(str(year)) == len(year_digits_set):
        print(year)
        break