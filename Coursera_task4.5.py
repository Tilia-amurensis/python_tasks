n = int(input())


def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

if IsPrime(n):
    print("yes")
else:
    print("no")
