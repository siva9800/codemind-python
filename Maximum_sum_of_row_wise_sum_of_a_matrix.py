n,m=map(int,input().split())
mat=[[int(i) for i in input().split()][:m] for j in range(n)]
maxi=0
for i in range(n):
    maxi=max(sum(mat[i]),maxi)
print(maxi)