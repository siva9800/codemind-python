n=int(input())
l=list(map(int,input().split()))
i=0
p=0
while i<(n-1):
    #local minima
    while i<(n-1) and l[i+1]<=l[i]:
        i+=1
    if i==n-1:
        break
    buy=i
    i+=1
    #local maxima
    while i<n and l[i]>=l[i-1]:
        i+=1
    sell=i-1
    p+=(l[sell]-l[buy])
print(p)