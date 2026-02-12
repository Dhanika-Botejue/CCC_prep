import sys

data = sys.stdin.read()
lines = data.splitlines()

amount = int(lines[0])
heights = lines[1].split()
int_heights = sorted([int(item) for item in heights])

#print(int_heights)
if amount % 2 == 0:
    halfway = amount // 2
else:
    halfway = amount // 2 + 1

lows = int_heights[:halfway]
lows.reverse()
highs = int_heights[halfway:]

new = []
low_counter = 0
high_counter = 0
#print(lows, highs)
for i in range(amount):
    if i % 2 == 0:
        new.append(lows[low_counter])
        low_counter += 1
    else:
        new.append(highs[high_counter])
        high_counter += 1
    #print(new)

print(*new)
        