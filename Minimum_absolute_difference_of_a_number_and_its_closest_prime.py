def prime(n):
    if n==1:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
def nxtprime(n):
    while prime(n)==False:
        n+=1
    return n
def preprime(n):
    while prime(n)==False:
        n-=1
    return n
n=int(input())
if prime(n):
    print(0)
else:
    print(min((n-preprime(n)),(nxtprime(n)-n)))