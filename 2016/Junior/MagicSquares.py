import sys

data = sys.stdin.read()
lines = data.splitlines()

count = 0
print_statement = False
for i in range(4):
    count = 0
    for j in range(4):
        count += int(lines[i].split(" ")[j])
    if i == 0:
        previous_count = count
    elif previous_count != count:
        print("not magic")
        print_statement = True
        break
if print_statement == False:
    for i in range(4):
        count2 = 0
        for j in range(4):
            count2 += int(lines[j].split(" ")[i])
        
        if count2 != count:
            print("not magic")
            print_statement = True
            break

if print_statement == False:
    print("magic")