import sys

lines = sys.stdin.read().split()

encoded = lines[0]
c_th_character = int(lines[1])

decoded = ""
tmp_number = ""
tmp_char = ""

# build decoded
for char in encoded:
    if char.isdigit() == False:
        # check if first time 
        if tmp_number == "":
            tmp_char = char
            continue
        else:
            decoded += (int(tmp_number) * tmp_char)
            tmp_char = char # new letter
            tmp_number = ""
    else:
        tmp_number += char

# last letter to add
decoded += (int(tmp_number) * tmp_char)
        
length = len(decoded)

#print(decoded, c_th_character, length)


answer = decoded[c_th_character % length]

print(answer)

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