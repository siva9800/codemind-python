n=int(input())
l=list(map(int,input().split()))
s=sorted(list(set(l)))
if len(s)>2:
    print(s[-3])
else:
    print(max(s))