money = int(input())
coins = int(input())
cakes = int(input())
current_coins = money*100+coins
cost = cakes * current_coins
print(cost // 100, cost % 100)
