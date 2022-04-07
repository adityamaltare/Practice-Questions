def operation(n,m,o):
    if (o==1):
        return n+m
        
    if (o==2):
        return n-m
        
    if (o==3):
        return n*m
        
    if (o==4):
        return n/m
flag=True                
while(flag==True):    
    n = int(input("enter 1st no. ="))
    m = int(input("enter 2nd no. ="))
    o = int(input("enter number beside operation to perform \n 1. add \n 2. substract \n 3. multiply \n 4. divide \n"))

    print(operation(n,m,o))
    pl=input("do you want to try again?(y/n)")
    if(pl=="y"):
        flag=True
    else:
        flag=False
    