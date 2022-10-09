n=int(input())
l=list(map(int,input().split()))
s=1
for i in range(n):
    s=s*l[i]
for i in range(n):
    print(s//l[i],end=' ')