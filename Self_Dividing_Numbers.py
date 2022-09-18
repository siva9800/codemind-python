def selfd(n):
    t=n
    while n>0:
        r=n%10
        if r==0 or t%r!=0:
            return False
        n//=10
    return True
m=int(input())
n=int(input())
for i in range(m,n+1):
    if selfd(i):
        print(i,end=' ')