import sys

data = sys.stdin.read()
lines = data.splitlines()

text = lines[0]
cyclic_shift = lines[1]

length = len(cyclic_shift)
shifts = [None] * length 

for i in range(length):
    end_part = cyclic_shift[0]
    cyclic_shift = cyclic_shift[1:]
    cyclic_shift = cyclic_shift + end_part
    shifts[i] = (cyclic_shift)

amount = len(text) - length + 1
yes = False
for i in range(length):
    if yes == True:
        break
    for j in range(amount):
        if text[j:j+length] == shifts[i]:
            print("yes")
            yes = True
            break


if yes == False:
    print("no")
