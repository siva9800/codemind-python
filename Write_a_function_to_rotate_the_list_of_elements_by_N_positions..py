n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=k%n
for i in range(c):
    v=l.pop()
    l.insert(0,v)
print(*l)