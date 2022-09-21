def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
a,b=map(int,input().split())
print(gcd(a,b))