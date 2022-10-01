n=int(input())
l=list(map(int,input().split()))
s=sorted(l,reverse=True)
v=[0]*n
i=1
j=0
if len(s)%2!=0:
    v[-1]=s[-1]
while i<n and j<n:
    v[i]=s[j]
    v[i-1]=s[j+1]
    i+=2
    j+=2
print(*v)