def pro(n):
    s=1
    p=0
    while n>0:
        r=n%10
        p+=r
        s=s*r
        n//=10
    return s-p
n=int(input())
print(pro(n))