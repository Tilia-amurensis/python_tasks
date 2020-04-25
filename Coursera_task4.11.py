def alina():
    n = int(input())
    if n == 0:
        print(n)
    else:
        alina()
        print(n)

alina()
