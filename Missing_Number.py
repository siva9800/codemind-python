n=int(input())
l=list(map(int,input().split()))
nn=n*(n+1)//2
print(nn-sum(l))