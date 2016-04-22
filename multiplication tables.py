num = int(input("Enter a number"))

def tables(n):
    for x in range(1, 11):
        print(n, "*", x, "=", n*x)

tables(num)
