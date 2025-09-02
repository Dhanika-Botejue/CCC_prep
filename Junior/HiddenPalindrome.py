import sys

data = sys.stdin.read()
lines = data.splitlines()

text = lines[0]

def palindrome(word):
    length = len(word)
    list_text = []
    for i in range(length):
        list_text.append(word[i])
    
    reversed_word = []
    for i in range(length):
        reversed_word.append(word[- i - 1]) 
    
    word = "".join(list_text)
    reversed_word = "".join(reversed_word)
    
    #print(word, reversed_word)
    if word == reversed_word:
        return True
    return False
   
length = len(text)
print_statement = False
for i in range(length):
    checks = i + 1
    
    length_test = length - i
    for j in range(checks):
        if palindrome(text[j:(length_test + j)]) == True and print_statement == False:
            print(length_test)
            print_statement = True  # stopping additional prints
            break
    if print_statement == True:
        break

