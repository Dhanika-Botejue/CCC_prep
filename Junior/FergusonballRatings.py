import sys

data = sys.stdin.read()
lines = data.splitlines()

players = int(lines[0])
gold_amount = 0
gold_team = ""
player_stars = 0

for i in range(players*2):
    if ((i+1) % 2 == 1):
        player_stars += int(lines[i+1]) * 5
    else:
        player_stars -= int(lines[i+1]) * 3
        if player_stars > 40:
            gold_amount += 1
        # reset
        player_stars = 0

if gold_amount == players:
    gold_team = "+"

print(f"{gold_amount}{gold_team}")
