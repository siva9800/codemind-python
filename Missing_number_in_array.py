for  _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l=sorted(l)
    t=True
    for i in range(1,len(l)):
        if abs(l[i-1]-l[i])!=1:
            print(l[i-1]+1)
            t=False
    if t==True:
        print(l[-1]+1)
    
    