u=int(input())
#m=[[str(i) for i in input().split()][:u] for j in range(u)]
m=[]
for i in range(u):
    p=list(map(str,input().split()))
    m.append(p)
c=[i.pop() for i in m]
print(c.pop())
    