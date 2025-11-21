import sys

data = sys.stdin.read()
lines = data.splitlines()

boiling_temp = int(lines[0])
pressure = boiling_temp * 5 - 400
print(pressure)

if pressure == 100:
    print(0)
elif pressure < 100:
    print(1)
else:
    print(-1)

