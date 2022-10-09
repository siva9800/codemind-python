n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(*[i+j for i,j in zip(a,b)])