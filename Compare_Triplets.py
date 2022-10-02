l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s=0
c=0
for i in range(len(l1)):
    if l1[i]>l2[i]:
        s=s+1
    if l1[i]<l2[i]:
        c+=1
print(s,c)