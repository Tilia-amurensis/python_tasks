p = float(input())
x = float(input())
y = float(input())
a = x * 100 + y
b = a + (a * p / 100)
print(int(b // 100), int(b % 100))
