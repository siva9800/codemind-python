n=input().lower()
m=input().lower()
n1=list(n)
m1=list(m)
v1=[i for i in m1 if i!=' ' and i in n1]
v=[i for i in n1 if i!=' ' and i in m1]
c=set(v1+v)
print(len(c))