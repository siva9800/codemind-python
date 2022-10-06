n=int(input())
l=list(map(int,input().split()))
s=sorted(l)
for i in l:
    v=s.index(i)
    print(v,end=' ')