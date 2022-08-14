n=int(input())
l=[int(x) for x in input().split()]
a=sorted([i for i in l if l.count(i)==1])
print(*a)