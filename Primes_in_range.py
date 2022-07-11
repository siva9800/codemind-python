def prime(a):
    if a==1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    else:
        return True
c=0
n=int(input())
m=int(input())
for i in range(n,m+1):
    if prime(i)==True:
        c=c+1
print(c)