r,c=map(int,input().split())
mat=[]
for i in range(r):
    l=list(map(int,input().split()))
    mat.append(l)
res = [max(idx) for idx in zip(*mat)]
for i in res:
    print(i)