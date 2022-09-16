n=input().lower()
m=input().lower()
n1=list(n)
m1=list(m)
v=[i for i in n1 if i!=' ' and i in m1]
v1=[i for i in m1 if i!=' ' and i in n1]
c=set(v+v1)
c1=sorted(list(c))
if len(c1)>0:
    print(''.join(c1))
else:
    print('-1')