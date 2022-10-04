r=int(input())
c=int(input())
c=0
for i in range(r):
    l=list(map(int,input().split()))
    c+=sum(l)
print(c)
