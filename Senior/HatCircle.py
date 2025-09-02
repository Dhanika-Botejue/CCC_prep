# THE INPUT ERROR WAS WITH MY DIVISION. BEFORE IT WAS GIVING A FLOAT (e.g. 4 / 2 = 2.0). 
# WITH FLOOR DIVISION ITS FINE (e.g 4 // 2 = 2)
import sys

lines = sys.stdin.read().split()

people = int(lines[0])
half = (people // 2)
counter = 0

for i in range(half):
    if lines[i+1] == lines[i+1+half]:
        counter += 2

print(counter)