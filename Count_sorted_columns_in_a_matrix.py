r,c=map(int,input().split())
mat1=[[int(i) for i in input().split()][:c] for j in range(r)]
v=[]
t=v
co=0
for i in range(c):
    for j in range(r):
        v.append(mat1[j][i])
for i in range(c):
    l=v[:r]
    if sorted(l)==l or sorted(l,reverse=True)==l:
        co+=1
    v=v[r:]
print(co)