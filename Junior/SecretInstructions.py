import sys

data = sys.stdin.read()
lines = data.splitlines()

instructions_going = True
i = 0
while instructions_going == True:
    instruction = lines[i]
    
    if instruction == "99999":
        break  
    
    direction_digits = instruction[:2]
    direction = int(direction_digits[0]) + int(direction_digits[1])
    if direction != 0:
        if direction % 2 == 0:
            steps = instruction[2:]
            movement = "right"
            print(f"right {steps}")
        else:
            steps = instruction[2:]
            movement = "left"
            print(f"left {steps}")
    else:
        steps = instruction[2:]
        print(f"{movement} {steps}")

    i += 1