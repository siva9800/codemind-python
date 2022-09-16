n=input().lower().split()
m=input().lower().split()
n1=[i for i in n if i in m]
m1=[i for i in m if  i in n]
print(len(set(n1+m1)))