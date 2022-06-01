n,k=map(int,input().split())
m=list(map(int,input().split()))
c=0
for i in m:
    if i<0:
        i=-i
    if len(str(i))==k:
        c=c+1
print(c)