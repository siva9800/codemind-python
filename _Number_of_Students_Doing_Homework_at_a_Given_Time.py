l1=int(input())
s=list(map(int,input().split()))
l2=int(input())
e=list(map(int,input().split()))
q=int(input())
c=0
for i in  range(l2):
    if  s[i]<=q and e[i]>=q:
        c+=1
print(c)