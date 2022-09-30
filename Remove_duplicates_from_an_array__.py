n=int(input())
l=list(map(int,input().split()))
print(*sorted(list(set(l))))