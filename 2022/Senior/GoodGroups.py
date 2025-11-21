import sys

data = sys.stdin.read()
lines = data.splitlines()

# together mulit-dimensional list 
must_together_amount = int(lines[0])

must_together = [None] * must_together_amount
for i in range(must_together_amount):
    must_together[i] = [None] * 2

for i in range(must_together_amount):
    for j in range(2):
        must_together[i][j] = (lines[i+1].split(" "))[j]

# not_together multi-dimensional list
not_together_amount = int(lines[must_together_amount+1])

not_together = [None] * not_together_amount
for i in range(not_together_amount):
    not_together[i] = [None] * 2

for i in range(not_together_amount):
    for j in range(2):
        not_together[i][j] = (lines[i+2+must_together_amount].split(" "))[j]


# setting groups
groups_amount = int(lines[must_together_amount+not_together_amount+2])
groups = [[None]] * groups_amount 

for i in range(groups_amount):
    groups[i] = lines[must_together_amount+not_together_amount+3+i]


# constraints broken count
constraints_broke = 0
checker1 = ""
checker2 = ""

# count from must together
for i in range(must_together_amount):
    checker1 = must_together[i][0]
    checker2 = must_together[i][1]
    for j in range(groups_amount):
        group_members = groups[j].split(" ")
        if checker1 in group_members and checker2 not in group_members:
            constraints_broke += 1
            break
# count from not together
for i in range(not_together_amount):
    checker1 = not_together[i][0]
    checker2 = not_together[i][1]
    for j in range(groups_amount):
        group_members = groups[j].split(" ")
        if checker1 in group_members and checker2 in group_members:
            constraints_broke += 1
            break

print(constraints_broke)
