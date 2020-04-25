def power(a, n):
    if n == 0:
        return 1
    if a == 0:
        return 0
    num = a
    if n > 1:
        num = num * power(a, n - 1)
    return num


a = float(input())
n = int(input())
print(power(a, n))
