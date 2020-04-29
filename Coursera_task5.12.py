a = list(map(int, input().split()))
for i in range(1, len(a), 2):
    temp = a[i - 1]
    a[i - 1] = a[i]
    a[i] = temp
print(*a)
