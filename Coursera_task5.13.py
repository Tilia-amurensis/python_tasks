size = int(input())
arr = list(map(int, input().split()))
num = int(input())
count = arr.count(num)
if count == 0:
    dif = None
    res = None
    for i in range(0, len(arr)):
        if dif is None and res is None:
            dif = abs(arr[i] - num)
            res = arr[i]
        else:
            temp_dif = abs(arr[i] - num)
            if temp_dif < dif:
                dif = temp_dif
                res = arr[i]
    print(res)
else:
    print(num)
