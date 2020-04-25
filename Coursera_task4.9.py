def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)


def ReduceFraction(n, m):
    a = gcd(n, m)
    p = n // a
    q = m // a
    return p, q


n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
