my_list = list(map(int, input().split()))
count_list = [0] * 101
for i in my_list:
    count_list[i] += 1
for j in range(101):
    count = count_list[j]
    if count > 0:
        print((str(j) + " ") * count, end="")
