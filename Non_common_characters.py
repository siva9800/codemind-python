n=input().lower()
m=input().lower()
n1=list(n)
m1=list(m)
v=[i for i in n1 if i!=' ' and i not in m1]
v1=[i for i in m1 if i!=' ' and i not in n1]
c=set(v+v1)
print(len(c))