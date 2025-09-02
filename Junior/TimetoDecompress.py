import sys

data = sys.stdin.read()
lines = data.splitlines()

amount_times = int(lines[0])

for i in range(amount_times):
    amount, char = lines[i+1].split(" ")
    amount = int(amount)
    print(char * amount)