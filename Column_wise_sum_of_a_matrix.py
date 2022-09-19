n,m=map(int,input().split())
mat=[[int(i) for i in input().split()][:m] for j in range(n)]
s=0
for i in range(m):
    for j in range(n):
        s+=(mat[j][i])
    print(s,end=' ')
    s=0