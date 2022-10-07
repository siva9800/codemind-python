n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    d[i]=d.get(i,0)+1
items=sorted(list(d.items()))
ans=sorted(items,reverse=True,key=lambda x:x[1])
for i in ans:
    print(i[0],end=' ')