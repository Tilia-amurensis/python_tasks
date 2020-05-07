hamlet = int(input())
dist1 = list(map(int, input().split()))
shelter = int(input())
dist2 = list(map(int, input().split()))
dist_ham = []
for i in range(dist1):
    list_hamlet = (dist1[i], i)
    dist_ham.append(list_hamlet)
dist_shelt = []
for i in range(dist2):
    list_shelter = (dist2[i], i)
    dist_shelt.append(list_shelter)
dist_ham.sort()
dist_shelt.sort()
print(dist_ham, dist_shelt)