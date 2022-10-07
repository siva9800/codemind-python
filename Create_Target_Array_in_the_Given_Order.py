l1=int(input())
n=list(map(int,input().split()))
l2=int(input())
i=list(map(int,input().split()))
ans=[]
k=0
for j in i:
    ans.insert(j,n[k])
    k+=1
print(*ans)