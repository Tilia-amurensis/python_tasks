hugehairypants = ['огромные', 'волосатые', 'штаны']
for i in hugehairypants:
    print(i)
    for j in hugehairypants:
         print(j)

magic_coins = 70
found_coins = 20
stolen_coins = 3
coins = found_coins
for week in range(1,53):
    coins = coins + magic_coins - stolen_coins
    print('Week %s = %s' % (week, coins))

for x in range(0, 20):
    print('привет %s' % x)
    if x < 9:
        break

x = 1
while x <= 25:
    x = x + 2
    print(x)

ingredients = ['bread', 'cheese', 'salat', 'salmon', 'batter']
ingridients_size = len(ingredients)
print("length ingridients:", ingridients_size)
for x in range(ingridients_size):
    print(x, ingredients[x])

weight = 57
lun_weight = weight
for year in range(1,16):
    lun_weight=lun_weight*0.165
    print('Year %s = %s'% (year, lun_weight))
