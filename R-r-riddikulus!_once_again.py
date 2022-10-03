a,b=map(int,input().split())
l=list(map(int,input().split()))
b=b%a
for i in range(b):
    k=l.pop(0)
    l.insert(a,k)
print(*l)