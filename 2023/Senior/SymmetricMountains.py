import sys

data = sys.stdin.read()
lines = data.splitlines()

total_length = int(lines[0])
heights = lines[1].split()
# converting to ints
for i in range(total_length):
    heights[i] = int(heights[i])

symmetres = [float("inf")] * total_length       # symmetres[i] is the lowest asymmetrical rating of length i + 1

#print(symmetres)
#print(total_length)
#print(heights)

# center of one mountain loop (odds)
for i in range(total_length):
    running_total = 0
    l = i
    r = i
    # expanding sides
    while l >= 0 and r < total_length:
        cur_size = r - l + 1
        #print(f"LEFT: {l}, RIGHT: {r}")

        # dp logic
        cur_addition = abs(heights[l] - heights[r])
        running_total += cur_addition
        #print(cur_addition, running_total)

        if running_total < symmetres[cur_size - 1]:
            #print("CHANGED")
            symmetres[cur_size - 1] = running_total

        # length + 2
        l -= 1
        r += 1


# center of two mountains loop (evens)
for i in range(total_length):
    running_total = 0
    l = i - 1
    r = i
    # expanding sides
    while l >= 0 and r < total_length:
        cur_size = r - l + 1
        #print(f"LEFT: {l}, RIGHT: {r}")

        # dp logic
        cur_addition = abs(heights[l] - heights[r])
        running_total += cur_addition
        #print(cur_addition, running_total)

        if running_total < symmetres[cur_size - 1]:
            #print("CHANGED")
            symmetres[cur_size - 1] = running_total

        # length + 2
        l -= 1
        r += 1



print(*symmetres)
