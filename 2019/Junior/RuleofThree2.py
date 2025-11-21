import sys

data = sys.stdin.read()
lines = data.splitlines()

rule_1 = lines[0]
rule_2 = lines[1]
rule_3 = lines[2]
steps, initial_seq, final_seq = lines[3].split(" ")
steps = int(steps)

# Rules setup
start1, end1 = rule_1.split(" ")
start2, end2 = rule_2.split(" ")
start3, end3 = rule_3.split(" ")

# Rules mapping
starts = [start1, start2, start3]
ends = [end1, end2, end3]

def find_steps(current_seq, steps_remaining, path):
    # Base case: If no steps are left, check if the current sequence matches the final sequence
    if steps_remaining == 0:
        if current_seq == final_seq:
            return path  # Return the path of rule applications
        else:
            return None  # No valid path found

    # Try applying each rule
    for i in range(3):
        # Find all occurrences of the start substring
        start_index = 0
        while True:
            # Find the next occurrence of the start substring
            index = current_seq.find(starts[i], start_index)
            if index == -1:
                break  # No more occurrences

            # Replace the occurrence of the start substring with the end substring
            new_seq = current_seq[:index] + ends[i] + current_seq[index + len(starts[i]):]

            # Recursively call the function with the new sequence and one fewer step
            result = find_steps(new_seq, steps_remaining - 1, path + [(i + 1, index, new_seq)])

            # If a valid path is found, return it
            if result is not None:
                return result

            # Move to the next occurrence
            start_index = index + 1

    # If no rule leads to the final sequence, return None
    return None

# Call the recursive function
solution_path = find_steps(initial_seq, steps, [])

# Output the result
if solution_path is not None:
    for step, (rule, index, new_seq) in enumerate(solution_path, start=1):
        print(f"{rule} {index + 1} {new_seq}")
else:
    pass  # No solution found (should not happen for valid inputs)