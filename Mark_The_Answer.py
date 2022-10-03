a,b=map(int,input().split())
l=list(map(int,input().split()))
c=0
d=0
for i in l:
    if i>b:
        d+=1
    else:
        c+=1
    if d>1:
        break
print(c)