n = list(map(int, input().split()))
m = list(map(int, input().split()))
if len(n) <= 10**5:
    m.sort()
print(' '.join(map(str, m)))
