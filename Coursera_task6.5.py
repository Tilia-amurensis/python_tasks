inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
user_list = []
for line in inFile:
    bet = line.split()
    user_list.append((bet[0], bet[1], bet[3]))
user_list.sort(key=lambda surname: surname[0])
for entry in user_list:
    print(*entry, file=outFile)
    print(*entry)
inFile.close()
outFile.close()
