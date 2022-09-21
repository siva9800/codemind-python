def rev(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n//=10
    return s
n=int(input())
n1=rev(n)
print((n**2)==(rev(n1**2)))