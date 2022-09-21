n=int(input())
l=list(map(int,input().split()))
v=[]
for i in range(0,len(l),2):
    v.append(str(l[i])*(l[i+1]))
c=''.join(v)
print(*c)