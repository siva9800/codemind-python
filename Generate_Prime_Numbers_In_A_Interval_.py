def prime(n):
    if n==1:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if prime(i):
        print(i)