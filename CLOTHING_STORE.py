n=int(input())
l=list(map(int,input().split()))
s=set(l)
c=0
for i in s:
    c+=(l.count(i))//2
print(c)