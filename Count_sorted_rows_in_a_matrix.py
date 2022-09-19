r,c=map(int,input().split())
mat1=[[int(i) for i in input().split()][:c] for j in range(r)]
co=0
for i in range(r):
    if sorted(mat1[i])==mat1[i] or sorted(mat1[i],reverse=True)==mat1[i]:
        co+=1
print(co)