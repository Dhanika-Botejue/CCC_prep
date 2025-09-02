import sys

lines = sys.stdin.read().splitlines()

amount_pieces = int(lines[0])
pieces = list(map(int, lines[1].split()))
pieces.sort()


def one_to_length(list_check, amount):
    for i in range(amount):
        if list_check[i] != (i + 1):
            break
        if i == (amount - 1):
            return True
    return False

# special case
if one_to_length(pieces, amount_pieces):
    print(int(amount_pieces / 2), 1)


#print(pieces)

