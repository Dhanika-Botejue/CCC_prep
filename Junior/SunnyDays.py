import sys

data = sys.stdin.read()
lines = data.splitlines()

days = int(lines[0])
weather = [None] * days

for i in range(days):
    weather[i] = lines[i+1]

P_counter = 0
break_state = False
length = len(weather)
highest = 0

for i in range(days):
    start = i
    P_counter = 0
    break_state = False

    for j in range(i, length):

        if P_counter > 1:
            if ((j - start) - 1) > highest:    # DOWN BY ONE BECAUSE THIS IS SECOND OCCURENCE OF PRECIP, AND CAN ONLY TAKE ONE
                highest = (j - start) - 1
            break_state = True
            break
        if "P" == weather[j]:
            P_counter += 1
    # LESS THAN TWO PRECIP
    if break_state == False:
        if P_counter == 1:
            if highest < (length - i):
                highest = length - i
        elif P_counter == 0:
            if (length - i - 1) > highest:
                highest = (length - i - 1)



print(highest)



    
