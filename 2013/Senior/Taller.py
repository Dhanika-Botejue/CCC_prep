from collections import deque
import sys

data = sys.stdin.read()
lines = data.splitlines()

adjacent = dict()

people_amount, comparisons = lines[0].split()
people_amount = int(people_amount)
comparisons = int(comparisons)

for i in range(comparisons):
    x, y = lines[i+1].split()
    x = int(x)
    y = int(y)

    if x in adjacent:
        adjacent[x].append(y)
    else:
        adjacent[x] = [y]

#print(adjacent)


# helper function
def possible_reach(start, end, N):
    explored = [False] * N
    q = deque()
    if start in adjacent:
        q.extend(adjacent[start])

    found = False
    while q:
        new = q.popleft()
        # making sure to not get stuck in graph loop
        if explored[new-1] == True:
            continue
        else:
            explored[new-1] = True

        # found
        if new == end:
            found = True
            break
        # add to queue
        if new in adjacent:
            q.extend(adjacent[new])


    if found == True:
        return True
    return False



start, end = lines[comparisons+1].split()
start = int(start)
end = int(end)

start_to_end = possible_reach(start, end, people_amount)

# start taller than end
if start_to_end == True:
    print("yes")
else:
    end_to_start = possible_reach(end, start, people_amount)
    # check if end taller than start
    if end_to_start == True:
        print("no")
    # if both are False, then status is unknown
    else:
        print("unknown")



