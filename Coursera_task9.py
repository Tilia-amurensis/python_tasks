num = int(input())
sum = 0

while num % 10:
    n = num % 10
    sum = sum + n
    num = num // 10

print(sum)

# a = num % 10
# b = num % 100 // 10
# c = num // 100
# print(a+b+c)
