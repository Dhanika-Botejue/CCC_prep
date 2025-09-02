import sys

data = sys.stdin.read()
lines = data.splitlines()

days = int(lines[0])
weather = [None] * days

for i in range(days):
    weather[i] = lines[i+1]

amount = weather.count("S")
print(amount + 1)