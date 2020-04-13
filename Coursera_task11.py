minute = int(input())
current_hour = minute // 60
current_hour = current_hour % 24
current_min = minute % 60
print(current_hour, current_min)
