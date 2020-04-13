x = float(input())
y = float(input())
res_km = x
res_day = 1
while True:
    if res_km >= y:
        break
    p = (res_km / 100) * 10
    res_km = res_km + p
    res_day += 1
print(res_day)
