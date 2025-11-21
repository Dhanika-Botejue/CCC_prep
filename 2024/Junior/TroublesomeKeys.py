import sys

data = sys.stdin.read()
lines = data.splitlines()

input_text = lines[0]
output_text = lines[1]

length_before = len(input_text)
length_after = len(output_text)

bad_chars_input = []
bad_chars_output = []

for i in range(length_before):
    if input_text[i] not in output_text and input_text[i] not in bad_chars_input:
        bad_chars_input.append(input_text[i])

for i in range(length_after):
    if output_text[i] not in input_text:
        bad_chars_output.append(output_text[i])
        break


# silly key input and quiet key are in bad_chars_input, which has two characters.
# silly key output is in bad_chars_output.
if len(bad_chars_input) == 1:
    silly_key_input, silly_key_output = bad_chars_input[0], bad_chars_output[0]
    print(silly_key_input, silly_key_output)
    print("-")
else:
    refined_input = input_text.replace(bad_chars_input[0], bad_chars_output[0])
    refined_input = refined_input.replace(bad_chars_input[-1], "")

    if refined_input == output_text:
        silly_key_input, silly_key_output, quiet_key = bad_chars_input[0], bad_chars_output[0], bad_chars_input[-1]
    else:
        silly_key_input, silly_key_output, quiet_key = bad_chars_input[-1], bad_chars_output[0], bad_chars_input[0]
    
    print(silly_key_input, silly_key_output)
    print(quiet_key)