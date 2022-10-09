n=int(input())
arr=list(map(int,input().split()))
maxso=-9999999
cs=0
for i in range(n):
    cs+=arr[i]
    if cs>maxso:
        maxso=cs
    if cs<0:
        cs=0
print(maxso)
    