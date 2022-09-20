def rev(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n//=10
    return s
for _ in range(int(input())):
    n=int(input())
    print(n==rev(n))