import sys

def max(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    return b

def min(a, b):
    if a < b:
        return a
    elif b < a:
        return b
    return b
    
lines = sys.stdin.read().split()

length1 = int(lines[0])
width1 = int(lines[1])
length2 = int(lines[2])
width2 = int(lines[3])


print(min((max(length1, length2) * 2 + (width1 + width2) * 2), (max(width1, width2) * 2 + (length1 + length2) * 2)))