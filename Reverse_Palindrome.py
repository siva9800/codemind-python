def rev(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n//=10
    return s
n=int(input())
while True:
    x=n+rev(n)
    if x==rev(x):
        print(x)
        break
    else:
        n=x