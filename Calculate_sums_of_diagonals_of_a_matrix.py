n=int(input())
mat=[]
for i in range(n):
    l=list(map(int,input().split()))
    mat.append(l)
ps=0
ss=0
for i in range(n):
    for j in range(n):
        if i==j:
            ps+=mat[i][j]
        if i+j==(n-1):
            ss+=mat[i][j]
print('Principal Diagonal:{}'.format(ps))
print('Secondary Diagonal:{}'.format(ss))