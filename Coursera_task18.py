second = int(input())
minute = second // 60
current_hour = minute // 60
current_hour = current_hour % 24
current_min = minute % 60
current_sec = second % 60
print("%d:%02d:%02d" % (current_hour, current_min, current_sec))
