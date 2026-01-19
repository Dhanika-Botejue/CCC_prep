import sys

data = sys.stdin.read()
lines = data.splitlines()

together_amount = int(lines[0])
togethers = set()

# adding to togethers set
for i in range(together_amount):
    person_a, person_b = lines[i+1].split()
    #print(person_a, person_b)
    togethers.add((person_a, person_b))

not_together_amount = int(lines[together_amount+1])
not_togethers = set()

# adding to not_togethers set
for i in range(not_together_amount):
    person_a, person_b = lines[together_amount+2+i].split()
    #print(person_a, person_b)
    not_togethers.add((person_a, person_b))


# checking for constraints
violated_count = 0
length_together_constraint = len(togethers)
groups_amount = int(lines[together_amount+not_together_amount+2])

for i in range(groups_amount):
    a, b, c = lines[together_amount+not_together_amount+3+i].split()
    # not togethers
    if (a, b) in not_togethers or (b, a) in not_togethers:
        violated_count += 1
    if (a, c) in not_togethers or (c, a) in not_togethers:
        violated_count += 1
    if (b, c) in not_togethers or (c, b) in not_togethers:
        violated_count += 1

    # remove together constraints (for my count)
    if (a, b) in togethers or (b, a) in togethers:
        length_together_constraint -= 1
    if (a, c) in togethers or (c, a) in togethers:
        length_together_constraint -= 1
    if (b, c) in togethers or (c, b) in togethers:
        length_together_constraint -= 1

#print(violated_count, length_together_constraint)
#print("final answer:", violated_count + length_together_constraint)
print(violated_count + length_together_constraint)



