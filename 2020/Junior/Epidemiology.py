import sys

data = sys.stdin.read()
lines = data.splitlines()

people_needed = int(lines[0])
people_affected = int(lines[1])
spread_rate = int(lines[2])

found = True
new_people_affected = people_affected
days = 0
while found == True:
    people_affected *= spread_rate
    new_people_affected += people_affected
    days += 1
    #print(new_people_affected)
    if new_people_affected > people_needed:
        print(days)
        break

