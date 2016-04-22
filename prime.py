num = int(input("Enter a number \n"))

def prime(no):
    i = 1
    while i < int(round(no/2))+1:
        i = i + 1
        if int(no) % i == 0:
            return False
    return True

if prime(num):
    print(num, "is prime")
else:
    print(num, "is not prime")
