def prime(n):
    if n==1:
        return True
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
a=int(input())
b=int(input())
c=a+b
if prime(c):
    c+=1
while prime(c)==False:
    c+=1
print(c-(a+b))