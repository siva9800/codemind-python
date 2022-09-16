n=input().lower().split()
m=input().lower().split()
v=[i for i in m if i in n]
print(*v)