a, b = list(map(int, input().split()))
my_list = []
while b > 0:
    n = int(input())
    my_list.append(n)
    b -= 1
my_list.sort()
my_sum = 0
my_count = 0
for i in my_list:
    my_sum += i
    if my_sum > a:
        break
    my_count += 1
    if my_sum == a:
        break
print(my_count)
