a = list(map(int, input().split()))
b = min(a)
c = max(a)
bi = a.index(b)
ci = a.index(c)
a[bi] = c
a[ci] = b
print(*a)
