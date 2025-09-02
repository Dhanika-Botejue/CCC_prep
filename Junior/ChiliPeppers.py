import sys

data = sys.stdin.read()
lines = data.splitlines()


peppers_spice = {"Poblano" : 1500,
"Mirasol" : 6000,
"Serrano" : 15500,
"Cayenne" : 40000,
"Thai" : 75000,
"Habanero" : 125000}

amount = int(lines[0])
total = 0

for i in range(amount):
    total += peppers_spice.get(lines[i+1], 0)   # default value for safeness

print(total)