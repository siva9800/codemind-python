n=int(input())
flag=False
if n<0:
    n=n*(-1)
    flag=True
s=0
while n>0:
    t=n
    r=n%10
    s=(s*10)+r
    n//=10
if flag:
    print(s*(-1))
else:
    print(s)