import sys

data = sys.stdin.read()
lines = data.splitlines()

cryptic_string = lines[0] 
length = len(cryptic_string)

instructions = []

# loop setup
started = False
start_point = None
end_point = None

# splitting the combined instruction into singular instructions
for i in range(length):
    if cryptic_string[i].isalpha() == True and started == False:
        start_point = i
        started = True
    
    elif started == True and (i+1) < length and cryptic_string[i].isnumeric() == True and cryptic_string[i+1].isalpha() == True:
        end_point = i+1
        instructions.append(cryptic_string[start_point:end_point])
        # Reset
        started = False
    elif (i+1) == length:
        # end of string and there is no (i+1)
        instructions.append(cryptic_string[start_point:])
        started = False

instructions_amount = len(instructions)
instruction_length = 0


singular_instruction_end = 0

for i in range(instructions_amount):
    instruction_length = len(instructions[i])
    if "+" in instructions[i]:
        chord, group = instructions[i].split("+") # where i messed up
        print(f"{chord} tighten {group}")
    elif "-" in instructions[i]:
        chord, group = instructions[i].split("-") # where i messed up
        print(f"{chord} loosen {group}")        

        





