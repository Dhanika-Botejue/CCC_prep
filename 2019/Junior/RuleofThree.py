import sys

data = sys.stdin.read()
lines = data.splitlines()

rule_1 = lines[0]
rule_2 = lines[1]
rule_3 = lines[2]
steps, initial_seq, final_seq = lines[3].split(" ")
steps = int(steps)

# rules setup
start1, end1 = rule_1.split(" ")
start2, end2 = rule_2.split(" ")
start3, end3 = rule_3.split(" ")

# rules mapping
starts = [start1, start2, start3]
ends = [end1, end2, end3]

# multi dimensional True/False list
tested = [None] * 3
for i in range(3):
    tested[i] = [None] * 2
for i in range(3):
    for j in range(2):
        if (j % 2 == 0):
            tested[i][j] = starts[i]
        else:
            tested[i][j] = False


def find_steps(steps, initial_seq, final_seq): 
    # possible rules
    possible = []
    possible_outcome = []

    for i in range(3):
        if starts[i] in initial_seq:
            possible.append(starts[i])
            possible_outcome.append(ends[i])
    
    print(possible)
    print(possible_outcome)


find_steps(steps, initial_seq, final_seq)
 
