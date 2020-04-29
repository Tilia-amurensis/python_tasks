myList = list(map(int, input().split()))
for i in myList[::2]:
    print(i, end=" ")
