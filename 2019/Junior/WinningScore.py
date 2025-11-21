import sys

data = sys.stdin.read()
lines = data.splitlines()

a_threes = int(lines[0])
a_twos = int(lines[1])
a_ones = int(lines[2])

b_threes = int(lines[3])
b_twos = int(lines[4])
b_ones = int(lines[5])

a_score = a_threes * 3 + a_twos * 2 + a_ones 
b_score = b_threes * 3 + b_twos * 2 + b_ones

if a_score > b_score:
    print("A")
elif b_score > a_score:
    print("B")
else:
    print("T")
