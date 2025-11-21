import sys

data = sys.stdin.read()
lines = data.splitlines()

first_digit = lines[0]
second_digit = lines[1]
third_digit = lines[2]
fourth_digit = lines[3]

if first_digit not in ["8", "9"]:
    print("answer")
elif second_digit != third_digit:
    print("answer")
elif fourth_digit not in ["8", "9"]:
    print("answer")

else:
    print("ignore")
