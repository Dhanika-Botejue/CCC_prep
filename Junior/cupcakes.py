import sys

data = sys.stdin.read()
lines = data.splitlines()

# input
regular_boxes = int(lines[0])
small_boxes = int(lines[1])

print(regular_boxes*8+small_boxes*3-28)