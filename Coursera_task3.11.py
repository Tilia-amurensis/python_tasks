s = input()
s_list = [s, ]
for i in range(len(s_list)):
    first = s_list[i].partition("h")
    last = s_list[i].rpartition("h")
    print(first[0], last[2], sep="")
