def sandp(n):
    s=0
    p=1
    while n>0:
        r=n%10
        s+=r
        p*=r
        n//=10
    return s==p
n=int(input())
if sandp(n):
    print('Spy Number')
else:
    print('Not Spy Number')