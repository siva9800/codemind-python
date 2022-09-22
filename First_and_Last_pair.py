n=int(input())
l=list(map(int,input().split()))
i=0
la=len(l)-1
while i<la:
    print(l[i],l[la],end=' ')
    i+=1
    la-=1
if len(l)%2!=0:
    print(l[i],'0',end=' ')