n=int(input())
l=list(map(int,input().split()))
s=''.join([str(i) for i in l])
print(*list(str(int(s)+1)))