import sys

data = sys.stdin.read()
lines = data.splitlines()

minutes_spent = int(lines[0])
mins_in_12hrs = 720
total_variations = 31 

# THANKS TO THIS CODE I KNOW THERE ARE 31 POSSIBLE VARIATIONS
"""
total_variations = 0
test_string = 
for i in range(11):
    hour = i + 1
    hour = str(hour)
    #test_string = hour
    for j in range(60):
        if j < 10:
            minute = str(j)
            minute = "0" + minute
        else:
            minute = str(j)
        test_string = hour + minute
        length = len(test_string)
        common_dif_status = True
        for k in range(length):
            if k == 0:
                common_dif = int(test_string[0]) - int(test_string[1])
            elif k < (length - 1) and (int(test_string[k]) - int(test_string[k+1])) != common_dif:
                common_dif_status = False
                break
            elif k == (length - 1) and common_dif_status == True:
                total_variations += 1
                print(test_string)

total_variations += 1   # there is one variation inside the 12 hour, which I didn't look into
"""
variations_past = 0

# amount of times the all variations of clock have past
clock_loops = int(minutes_spent / mins_in_12hrs)
variations_past = clock_loops * total_variations

# find the remaining variations left
leftover_mins = minutes_spent - mins_in_12hrs * clock_loops

# all cases by minutes past since 12:00
times_past_amounts = [671, 591, 532, 520, 473, 461, 414, 402, 390, 355, 343, 331, 296, 284, 272, 260, 237, 225, 213, 201, 178, 166, 154, 142, 130, 119, 107, 95, 83, 71, 34]

for i in range(31):
    if leftover_mins >= times_past_amounts[i]:
        variations_past += (31 - i)
        break

print(variations_past)
