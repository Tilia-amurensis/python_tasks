import time

print(time.time())

def lots_of_numders(max):
    start = time.time()
    for x in range(0,max):
        print(x)
    end = time.time()
    print('Passed %s sec'% (end-start))
lots_of_numders(1000)

print(time.asctime())

t = (2020, 2, 23, 10, 30, 48, 6, 0, 0)
print(time.asctime(t))

print(time.localtime())

t = time.localtime()
year = t[0]
month = t[1]
print(year)
print(month)

for x in range(1, 61):
    print(x)
    time.sleep(1)