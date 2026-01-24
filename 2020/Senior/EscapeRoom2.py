import sys
from collections import deque


# Creating some helper functions

all_factors = dict()
def get_factors(number):
    global all_factors
    if number in all_factors:
        return all_factors[number]
    
    factors_together = set()

    for i in range(1, int(number**0.5) + 1):
        # found a factor
        if number % i == 0:
            n1 = i
            n2 = number // n1
            factors_together.add((n1, n2))
            factors_together.add((n2, n1))


    all_factors[number] = factors_together
    return factors_together

# input
data = sys.stdin.read()
lines = data.splitlines()

rows = int(lines[0])
columns = int(lines[1])

room = []
for i in range(rows):
    data = lines[i+2].split()
    row = [int(item) for item in data]
    room.append(row)

#print(room)  

explored = []
for i in range(rows):
    explored.append([False] * columns)
    

# NOTE for me: for adding right, use q.append(xxx), for popping left, use q.popleft() = saved
q = deque()


factors = get_factors(room[0][0])
for factor in factors:
    q.append(factor)

found = False

#print(q)
while q:
    indexing = q.popleft()
    r, c = indexing[0], indexing[1]

    # CCC question specifics
    r -= 1
    c -= 1

    if r == (rows - 1) and c == (columns - 1):
        found = True
        break

    #print(q, r, c)
    # check for valid indexing
    if 0 <= r < rows and 0 <= c < columns:
        if explored[r][c] == False:
            explored[r][c] = True
            number = room[r][c]
            
            factors = get_factors(number)
            for factor in factors:
                q.append(factor)

            #print(q)
    
            

if found == True:
    print("yes")
else:
    print("no")
    
