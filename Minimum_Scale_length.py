def gcd(a,b):
    mini=min(a,b)
    for i in range(1,mini+1):
        if a%i==0 and b%i==0:
            h=i
    return h
n=int(input())
l=list(map(int,input().split()))
a=l[0]
b=l[1]
gc=gcd(a,b)
for i in range(2,len(l)):
    gc=gcd(gc,l[i])
print(gc)