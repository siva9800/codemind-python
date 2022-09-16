n=input().lower().split()
m=input().lower().split()
m2=[i for i in n if n.count(i)==1]
n2=[i for i in m if m.count(i)==1]
n1=[i for i in n2 if i in m2]
m1=[i for i in m2 if  i in n2]
print(len(set(n1+m1)))