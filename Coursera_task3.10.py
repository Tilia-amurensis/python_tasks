word = input()
first = word.find("f")
last = word.rfind("f")
if first != -1 and last == first:
    print(first)
elif first != -1 and last != -1 and first != last:
    print(first, last)
else:
    pass
