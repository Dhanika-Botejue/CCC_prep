import sys

data = sys.stdin.read()
lines = data.splitlines()

hidden_word = lines[0]
length = len(hidden_word)
rows = int(lines[1])
columns = int(lines[2])
count = 0

# word-search in multidimensional array
characters = [None] * rows
for i in range(rows):
    characters[i] = [None] * columns

for i in range(rows):
    for j in range(columns):
        line = lines[i+3]
        line = line.replace(" ", "")
        characters[i][j] = line[j]

# horizontal checks
if length <= columns:
    for i in range(rows):
        normal = "".join(characters[i])             # list so must join first
        reversed = "".join(characters[i][::-1])     # list so must join first
        for j in range(columns - length + 1):        
            if hidden_word == normal[j:(length + j)]:
                count += 1
            if hidden_word == reversed[j:(length + j)]:
                count += 1
# vertical checks
if length <= rows:
    test_string = ""
    for i in range(columns):
        for j in range(rows):
            if j == 0:
                test_string = "" + characters[j][i]   # reset, but still add first char
            elif j > 0:
                test_string = test_string + characters[j][i]
        # string is the column at this point
        reversed = test_string[::-1]
        for k in range(rows - length + 1):
            if hidden_word == test_string[k:(length + k)]:
                count += 1
            if hidden_word == reversed[k:(length + k)]:
                count += 1

        


# i messed up, cuz i brute forced, but realized i didn't need to
for i in range(rows):
    for j in range(columns):
        if characters[i][j] == hidden_word[0]:
            top_left = True
            top_right = True
            bottom_left = True
            bottom_right = True
            for k in range(length - 1):
                # going bottom right
                if (i+k+1) > (rows-1) or (j+k+1) > (columns-1):
                    bottom_right = False
                elif characters[i+k+1][j+k+1] != hidden_word[k+1]:
                    bottom_right = False
                
                # going bottom left
                if (i+k+1) > (rows-1) or (j-k-1) < 0:
                    bottom_left = False   
                elif characters[i+k+1][j-k-1] != hidden_word[k+1]:
                    bottom_left = False

                # going top right
                if (i-k-1) < 0 or (j+k+1) > (columns-1):
                    top_right = False         
                elif characters[i-k-1][j+k+1] != hidden_word[k+1]:
                    top_right = False

                # going top left
                if (i-k-1) < 0 or (j-k-1) < 0:
                    top_left = False
                elif characters[i-k-1][j-k-1] != hidden_word[k+1]:
                    top_left = False
                
                # found word check
                if k == (length - 2):
                    if top_left == True:
                        count += 1
                    if top_right == True:
                        count += 1
                    if bottom_left == True:
                        count += 1
                    if bottom_right == True:
                        count += 1



print(count)

