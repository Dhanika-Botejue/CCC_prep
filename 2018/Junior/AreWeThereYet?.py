import sys

data = sys.stdin.read()
lines = data.splitlines()

city1 = 0
city2, city3, city4, city5 = lines[0].split(" ")
city2 = int(city2)
city3 = int(city3)
city4 = int(city4)
city5 = int(city5)

cities = [city1, city2, city3, city4, city5]

for i in range(5):
    if i == 0:
        print(f"0 {city1 + city2} {city1 + city2 + city3} {city1 + city2 + city3 + city4} {sum(cities)}")
    elif i == 1:
        print(f"{city2} 0 {city3} {city3 + city4} {city3 + city4 + city5}")
    elif i == 2:
        print(f"{city2 + city3} {city3} 0 {city4} {city4 + city5}") 
    elif i == 3:
        print(f"{city2 + city3 + city4} {city3 + city4} {city4} 0 {city5}")
    else:
        print(f"{sum(cities)} {sum(cities) - city2} {sum(cities) - city2 - city3} {city5} 0")
