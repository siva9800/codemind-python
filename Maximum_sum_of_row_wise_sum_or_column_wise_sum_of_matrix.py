r,c=map(int,input().split())
mat1=[]
for i in range(r):
    l=list(map(int,input().split()))
    mat1.append(l)
s,cs,rs=0,0,0
for i in range(c):
    for j in range(r):
        s+=mat1[j][i]
    cs=max(cs,s)
    s=0
for i in range(r):
    rs=max(rs,sum(mat1[i]))
print(max(cs,rs))