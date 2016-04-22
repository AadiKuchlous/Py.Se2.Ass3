word = input("Enter a word")

def palindrome(w):
    for i in range(len(w)):
        if w[i] != w[0-i-1]:
            return False
    return True

if palindrome(word):
    print(word, "is palindrome")
else:
    print(word, "is not palindrome")
