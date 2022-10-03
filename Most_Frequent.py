n=int(input())
l=list(map(int,input().split()))
s=sorted(list(set(l)))
a=[]
maxi=0
for i in s:
    v=l.count(i)
    a.append(v)
print(s[a.index(max(a))])