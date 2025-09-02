import sys

data = sys.stdin.read()
lines = data.splitlines()

lines_amount = int(lines[0])

for i in range(lines_amount):
    length = len(str(lines[i+1]))
    count = 0
    text = ""

    for j in range(length):        
        if j == 0:
            count += 1
            consecutive_char = lines[i+1][0]
        elif lines[i+1][j] != consecutive_char and (j+1) < length:
            if text == "":
                text += f"{count} {consecutive_char}"
            else:
                text += f" {count} {consecutive_char}"
            count = 1
            consecutive_char = lines[i+1][j]

        elif j == (length-1):
            if lines[i+1][j] == consecutive_char:
                count += 1
            else:
                # old unadded one
                text += f" {count} {consecutive_char}"
                
                consecutive_char = lines[i+1][j]
                count = 1
            
            text += f" {count} {consecutive_char}"
            print(text)

        else: 
            count += 1


            
