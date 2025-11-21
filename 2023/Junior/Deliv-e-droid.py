import sys

data = sys.stdin.read()
lines = data.splitlines()

delivered = int(lines[0])
collisions = int(lines[1])

score = (delivered * 50 - collisions * 10)

if delivered > collisions:
    score += 500

print(score)