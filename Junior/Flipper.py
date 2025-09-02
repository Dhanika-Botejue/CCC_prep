import sys

data = sys.stdin.read()
lines = data.splitlines()

flips = lines[0]
flips_amount = len(flips)

top = [1, 2]
bottom = [3, 4]

store_value1 = 0
store_value2 = 0
for i in range(flips_amount):
    if flips[i] == "H":
        store_value1 = top[0]
        top[0] = bottom[0]
        bottom[0] = store_value1

        store_value2 = top[1]
        top[1] = bottom[1]
        bottom[1] = store_value2
    else:
        store_value1 = top[0]
        top[0] = top[1]
        top[1] = store_value1

        store_value2 = bottom[0]
        bottom[0] = bottom[1]
        bottom[1] = store_value2


print(top[0], top[1])
print(bottom[0], bottom[1])