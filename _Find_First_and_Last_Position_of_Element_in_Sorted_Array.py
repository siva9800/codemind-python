def binaryLeft(arr,n,target):
    r=n-1
    l=0
    mid=0
    while l<=r:
        mid=(l+r)//2
        if  arr[mid]<target:
           l=mid+1
        else:
            r=mid-1
    return l
def binaryRight(arr,n,target):
    r=n-1
    l=0
    mid=0
    while l<=r:
        mid=(l+r)//2
        if arr[mid]<=target:
            l=mid+1
        else:
            r=mid-1
    return r
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
r=binaryRight(arr,n,target)
l=(binaryLeft(arr,n,target))
if l<=r:
    print(l,r)
else:
    print(-1,-1)