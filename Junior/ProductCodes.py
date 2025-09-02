import sys

data = sys.stdin.read()
lines = data.splitlines()

codes = int(lines[0])
capitals = []
integer = "0"
new_codes = []

continous_number = True
negative = False
final_num = 0

for i in range(codes):
    length = len(lines[i+1])
    capitals = []
    integer = 0
    negative = False
    continous_number = True
    final_num = 0
    continous_number_list = [None] * length
    for j in range(length):
        # Uppercase
        if lines[i+1][j].isupper():
            print(lines[i+1][j])
            capitals.append(lines[i+1][j])
            continous_number = False
        # Lowercase
        elif lines[i+1][j].isalpha():
            continous_number = False
        # Number
        elif lines[i+1][j].isnumeric():
            if continous_number == True:
                integer += str(lines[i+1][j])
            
            elif continous_number == False:
                integer = str(integer)
            
            if (j + 1) >= length:
                integer = int(integer)
                final_num += int(integer)
                print(integer)
                print(final_num)
                break
            if (j + 1) >= length: 
                # Negative
                if negative == True:
                    integer *= -1
                
                final_num += integer
                negative = False
                # New
                integer = lines[i+1][j]
                continous_number = True
            
            if lines[i+1][j+1].isalpha() or lines[i+1][j+1].isupper():
                integer = int(integer)
                if negative == True:
                    integer *= -1

                final_num += int(integer)
                print(capitals)
                print(capitals, final_num)
                break


        elif lines[i+1][j] == "-":
            negative = True
