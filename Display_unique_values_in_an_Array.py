n=int(input())
l=list(map(int,input().split()))
s=set(l)
f=True
for i in s:
    if l.count(i)==1:
        f=False
        print(i,end=' ')
if f:
    print('-1')