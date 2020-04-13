cow = int(input())
cow1 = cow % 10
if cow1 == 1 and cow != 11:
    print(cow, "korova")
elif cow1 > 1 and cow1 < 5 and cow != 12 and cow != 13 and cow != 14:
    print(cow, "korovy")
else:
    print(cow, "korov")
