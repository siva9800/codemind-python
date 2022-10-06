n=int(input())
l=list(map(int,input().split()))
s=set(l)
maxi=0
for i in s:
    if l.count(i)==1:
        if i>maxi:
            maxi=i
if maxi==0:
    print('-1')
else:
    print(maxi)