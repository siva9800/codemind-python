n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
v=[]
c=0
for i in b:
    if  i in  a and i not in v:
        c+=1
        v.append(i)
if c==len(b):
    print('Yes')
else:
    print('No')