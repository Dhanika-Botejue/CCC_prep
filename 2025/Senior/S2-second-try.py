import sys

lines = sys.stdin.read().split()

encoded = lines[0]
c_th_character = int(lines[1])

decoded = []
tmp_number = ""
tmp_char = ""

length = 0
# build decoded into list of tuples
for char in encoded:
    if char.isdigit() == False:
        # check if first time 
        if tmp_number == "":
            tmp_char = char
            continue
        else:
            decoded.append(((int(tmp_number)), tmp_char))
            length += int(tmp_number)
            tmp_char = char # new letter
            tmp_number = ""
    else:
        tmp_number += char

# last letter to add
decoded.append(((int(tmp_number)), tmp_char))
length += int(tmp_number)

#print(decoded)
wanted_index = c_th_character % length

current_index = 0
upcoming_index = 0

for mini_tuple in decoded:
    current_index = upcoming_index
    upcoming_index = current_index + mini_tuple[0]
    if current_index <= wanted_index < upcoming_index:
        print(mini_tuple[1])
        break
        

#print(decoded, c_th_character, length)


#answer = decoded[c_th_character % length]

#print(answer)

"""
1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 0
9 1
"""