n=int(input())
t=n
a=len(str(n))
s=0
while n>0:
    r=n%10
    s=s+(r**a)
    a-=1
    n//=10
print(t==s)