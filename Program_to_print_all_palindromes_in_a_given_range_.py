def palin(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n//=10
    return s
a=int(input())
b=int(input())
v=[i for i in range(a,b+1) if i==palin(i)]
print(' '.join([str(i) for i in v]))