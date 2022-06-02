n=int(input())
l=list(map(int,input().split()))
c=[]
s=0
for i in l:
    if len(str(i))>s:
        s=len(str(i))
m=[i for i in l if len(str(i))==s]
print(*m)
'''for i in l:
    if len(str(i))==s:
        print(i,end=' ')'''