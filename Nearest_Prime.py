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
for _ in range(int(input())):
    n=int(input())
    if prime(n):
        print(n)
    else:
        if (n-preprime(n))>(nxtprime(n)-n):
            print(nxtprime(n))
        else:
            print(preprime(n))