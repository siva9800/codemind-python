n=int(input())
for i in range(n+1):
    a,b=map(int,input().split())
    c=0
    for i in range(a,b+1):
        if i%10==2 or i%10==3 or i%10==9:
            c=c+1
    print(c)