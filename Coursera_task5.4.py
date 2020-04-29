n = int(input())

for i in range(1, n + 1):
    print(i)
    if i == n:
        break
    for i in range(1, i + 1):
        print(i, end="")
