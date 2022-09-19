n,m=map(int,input().split())
mat=[[int(i) for i in input().split()][:m] for j in range(n)]
maxi=0
s=0
for i in range(m):
    for j in range(n):
        s+=mat[j][i]
    maxi=max(maxi,s)
    s=0
print(maxi)