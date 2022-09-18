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
v=[i for i in range(1,n+1) if prime(i)==False and n%i==0]
print(len(v))