a = list(map(int, input().split()))
b = []
for num in a:
    if num > 0 and num != 0 and num < 1000:
        b.append(num)
print(min(b))
