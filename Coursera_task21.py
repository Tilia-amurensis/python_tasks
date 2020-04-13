high = int(input())
dayDist = int(input())
nightDist = int(input())
generalDist = 0
days = 0
while True:
    # print("Dist is:", generalDist)
    generalDist = generalDist + dayDist
    days = days + 1
    if generalDist < high:
        generalDist = generalDist - nightDist
    else:
        break
print(days)
