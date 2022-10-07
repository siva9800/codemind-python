n=int(input())
l=list(map(int,input().split()))
d={}
for i in range(1,n,2):
    if l[i] not in d:
        d[l[i]]=l[i-1]
    else:
        d[l[i]]+=l[i-1]
v=''.join([str(k)*v for k,v in d.items()])
print(*v)