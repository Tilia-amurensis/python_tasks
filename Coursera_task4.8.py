def power(a, n):
    if n == 0:
        return 1
    if a == 0:
        return 0
    num = a
    if n % 2 == 1:
        num = num * power(a, n - 1)
        return num
    if n % 2 == 0:
        return power(a, n / 2) ** 2


a = float(input())
n = int(input())
print(power(a, n))
