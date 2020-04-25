s = input()
num = 0
for i in range(len(s)):
    if s[i] == "f":
        num = num + 1
        if num == 2:
            print(i)
if num == 1:
    print("-1")
elif s.find("f") == -1:
    print("-2")
