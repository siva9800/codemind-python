n=int(input())
l=list(map(int,input().split()))
v=[]
c=[v.append(i) for i in l if i not in v]
if sorted(l)==l and l==v:
    print('yes')
else:
    print('no')