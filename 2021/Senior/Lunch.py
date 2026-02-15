import sys

lines = sys.stdin.read().splitlines()
amount = int(lines[0])

positions = []
speeds = []
hearing_distances = []

for i in range(amount):
    position, speed, hear = lines[i+1].split()
    positions.append(int(position))
    speeds.append(int(speed))
    hearing_distances.append(int(hear))

#print(positions)
#print(speeds)
#print(hearing_distances)

def check_cost(c, positions, speeds, hears):
    amount = len(positions)
    cost = 0
    for i in range(amount):
        # c is on person
        if c == positions[i]:
            continue
        # c is more right than person, but person can still hear
        elif c > positions[i] and (c - hears[i]) <= positions[i]:
            continue
        # c is more left than person, but person can still hear
        elif c < positions[i] and (c + hears[i]) >= positions[i]:
            continue

        # c is more right than person, and person cannot hear already
        elif c > positions[i]:
            cost += ((c - hears[i]) - positions[i]) * speeds[i]
        # c is more left, and person cannot hear already
        elif c < positions[i]:
            cost += (positions[i] - (c + hears[i])) * speeds[i]

    return cost

# range is from smallest position to biggest position
smallest = min(positions)
biggest = max(positions)

ans = check_cost(smallest, positions, speeds, hearing_distances)

while smallest <= biggest:
    cur_middle = (smallest + biggest) // 2

    # start from middle of range - check its cost
    cur_cost = check_cost(cur_middle, positions, speeds, hearing_distances)

    # go to middle of range + 1 - check its cost
    above_cur_cost = check_cost(cur_middle + 1, positions, speeds, hearing_distances)
    
    ans = min(ans, cur_cost, above_cur_cost)

    # if middle + 1 cost > middle cost, then the new range is existing bottom to middle
    if above_cur_cost > cur_cost:
        biggest = cur_middle - 1

    # else new range is middle to existing top
    elif above_cur_cost < cur_cost:
        smallest = cur_middle + 1

print(ans)



