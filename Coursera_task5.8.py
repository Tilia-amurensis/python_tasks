myList = list(map(int, input().split()))
prev_num = None
for num in myList:
    if prev_num is not None and num > prev_num:
        print(num, end=" ")
    prev_num = num
