n=int(input())
l=list(map(int,input().split()))
v=sorted([i**2 for i in  l])
print(*v)