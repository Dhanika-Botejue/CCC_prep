import sys

data = sys.stdin.read()
lines = data.splitlines()

anna_points = 100
david_points = 100
rounds = int(lines[0])

for i in range(rounds):
    rolls = lines[i+1].split(" ")
    anna_roll = int(rolls[0])
    david_roll = int(rolls[1])
    
    if anna_roll > david_roll:
        david_points -= anna_roll
    elif anna_roll < david_roll:
        anna_points -= david_roll
    
print(anna_points)
print(david_points)
