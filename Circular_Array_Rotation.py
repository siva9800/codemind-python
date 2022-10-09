def right(arr,k,n):
    k=k%n
    for i in range(k):
        a=arr.pop()
        arr.insert(0,a)
    return arr
n,k,q=map(int,input().split())
l=list(map(int,input().split()))
c=(right(l,k,n))
for i in range(q):
    a=int(input())
    print(c[a])