import sys

data = sys.stdin.read()
lines = data.splitlines()

target = int(lines[0])
#print(target)

# now all we must do is check if 0 to max_fives fives with fours to fill up remaining spots works
max_fives = target // 5

amount_ways = 0

for i in range((max_fives + 1)):
    four_reach = target - i * 5
    if four_reach % 4 == 0:
        amount_ways += 1

print(amount_ways)





