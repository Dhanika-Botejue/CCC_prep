import sys

data = sys.stdin.read()
lines = data.splitlines()

total_time = int(lines[0])
total_chores = int(lines[1])

chores = [None] * total_chores

chores_count = 0
time_count = 0

for i in range(total_chores):
    chores[i] = int(lines[i+2])

chores.sort()

for i in range(total_chores):
    time_count += chores[i]
    if time_count <= total_time:
        chores_count += 1
    else:
        break

print(chores_count)
    