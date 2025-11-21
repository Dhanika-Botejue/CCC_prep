import sys

data = sys.stdin.read()
lines = data.splitlines()

input_text = lines[0]
output_text = lines[1]

# Convert output_text to a set for O(1) membership checking
input_set = set(input_text)
output_set = set(output_text)

# Find the quiet key (a key pressed but never displayed)
bad_chars_input = []
for char in set(input_text):  # Avoid duplicate checks
    if char not in output_set:
        bad_chars_input.append(char)

# Find the silly key and its wrong output
bad_chars_output = []
length = len(output_set)
input_unique = list(input_set)
output_unique = list(output_set)
for i in range(length):
    if output_unique[i] not in input_unique:  
        bad_chars_output.append(output_unique[i])
        break  # Only need one example of wrong output

# Determine the silly and quiet keys
if len(bad_chars_input) == 1:
    silly_key_input, silly_key_output = bad_chars_input[0], bad_chars_output[0]
    print(silly_key_input, silly_key_output)
    print("-")
else:
    # Check which bad input character is the silly key
    first_bad, second_bad = bad_chars_input
    refined_input = input_text.replace(first_bad, bad_chars_output[0]).replace(second_bad, "")

    if refined_input == output_text:
        silly_key_input, silly_key_output, quiet_key = first_bad, bad_chars_output[0], second_bad
    else:
        silly_key_input, silly_key_output, quiet_key = second_bad, bad_chars_output[0], first_bad

    print(silly_key_input, silly_key_output)
    print(quiet_key)
