n= int(input())
names= list(map(str,input().split()))
newnames = names[::-1]
for i in newnames:
    print(i)
    