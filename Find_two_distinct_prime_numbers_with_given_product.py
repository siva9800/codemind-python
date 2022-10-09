def prime(n):
    if n==1:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
n=int(input())
v=[]
for i in range(1,n):
    if n%i==0 and prime(i):
        v.append(i)
if len(v)==0:
    print('-1')
else:
    print(*v)
