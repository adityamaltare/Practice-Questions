n= int(input())
names= list(map(str,input().split()))
mid = int(n/2)

newlist= names[mid:]
alist= names[0:mid]
for i in range(len(names[0:mid])):
    newlist.append(alist[i])

for i in newlist:
    print(i)
    