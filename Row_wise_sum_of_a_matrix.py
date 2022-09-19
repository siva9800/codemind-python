n,m=map(int,input().split())
mat=[[int(i) for i in input().split()][:m] for j in range(n)]
for i in range(n):
    print(sum(mat[i]),end=' ')