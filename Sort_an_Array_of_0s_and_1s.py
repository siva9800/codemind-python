n=int(input())
l=list(map(int,input().split()))
vis=[]
for i in l:
    if i==0:
        vis.append(i) 
for i in l:
    if i==1:
        vis.append(1)
print(*vis)