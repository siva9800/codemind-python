def prime(n):
    if n==1:
        return 'not a prime'
    i=2
    while i*i<=n:
        if n%i==0:
            return 'not a prime'
        i+=1
    return 'prime'
n=int(input())
print(prime(n))