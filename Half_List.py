n=int(input())
l=list(map(int,input().split()))
v=[0]*n
j=0
k=n-1
i=0
while j<n//2 and i<n:
    v[i]=l[k]
    if i>=(n//2):
        v[i]=l[j]
        j+=1
    i+=1
    k-=1
print(*v)