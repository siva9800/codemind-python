n,k=map(int,input().split())
m=list(map(int,input().split()))
c=0
for i in m:
    if i%k==0:
        c+=1
print(c)
