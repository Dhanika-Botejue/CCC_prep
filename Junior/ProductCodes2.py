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
            capitals.append(lines[i+1][j])
            continous_number = False
            negative = False
        # Lowercase
        elif lines[i+1][j].islower():
            continous_number = False
            negative = False
        elif lines[i+1][j] == "-":
            continous_number = False
            negative = True
        # Number
        elif lines[i+1][j].isnumeric():
            if continous_number == False:
                integer = str(lines[i+1][j])
                continous_number = True     
            elif continous_number == True:
                integer = str(integer) + str(lines[i+1][j])
            
            if (j + 1) == length:
                integer = int(integer)
                if negative == True:
                    integer *= -1

                final_num += integer
                
            
            elif lines[i+1][j+1].isupper() or lines[i+1][j+1].islower() or lines[i+1][j+1] == "-":
                integer = int(integer)
                if negative == True:
                    integer *= -1
                final_num += integer
    
    print(str(("").join(capitals)) + str(final_num))



            
