def fact(k):
    c=0
    for i in range(1,k+1):
        if k%i==0:
            c+=i
    return c
k=input()
c=(k.replace(',',''))
l=[int(x) for x in c]
v=[]
for i in l:
    if fact(i) in l:
        v.append(i)
if len(v)>=1:
    print(*sorted(v))
else:
    print('-1')