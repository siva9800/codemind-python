v=[]
n=int(input())
for i in range(n):
    a=int(input())
    v.append(a)
c=int(input())
co=0
for i in  v:
    if i<=c:
        co+=1
    else:
        co+=2
print(co)