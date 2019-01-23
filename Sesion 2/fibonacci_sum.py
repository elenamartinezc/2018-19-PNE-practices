def fibonacci(n):
    a = 0
    b = 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

n = int(input("Enter a valid number"))
fibonacci(n)
