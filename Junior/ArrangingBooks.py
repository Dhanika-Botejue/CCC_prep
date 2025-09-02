import sys

data = sys.stdin.read()
lines = data.splitlines()

books_str = lines[0]
amount = len(books_str)
books = [None] * amount

# Zero case
if books_str == ''.join(sorted(books_str)):
    print(0)

else:
    swaps = 0
    for i in range(amount):
        books[i] = books_str[i]

    large_books = True # to remove starting large books from list
    new_amount_large = amount # to not mess with the for loop
    for i in range(amount):
        if large_books == True and books[0] == "L":
            del books[0]
            new_amount_large -= 1
        else:
            large_books = False
            break
    
    small_books = True
    new_amount_small = new_amount_large
    for i in range(new_amount_large):
        if small_books == True and books[-1] == "S":
            del books[-1]
            new_amount_small -= 1
        else:
            small_books = False
            break
    # algorithm once the sorted books are cut off
    amount = new_amount_small
    for i in range(int(amount / 2)):
        if books == sorted(books):
            break
        else:
            del books[i]
            books.pop()
            new_amount_small -= 2

            swaps += 1
            
            large_books = True
            small_books = True

            for j in range(new_amount_small):
                if large_books == True and books[0] == "L":
                    del books[0]
                    new_amount_small -= 1
                else:
                    large_books = False
                    break
            for k in range(new_amount_small):
                if small_books == True and books[-1] == "S":
                    del books[-1]
                    new_amount_small -= 1
                else:
                    small_books = False
                    break

    
    print(swaps)






