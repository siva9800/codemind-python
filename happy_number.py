n=int(input())
def happ(n):
    s=0
    while n>0:
        r=n%10
        s+=(r**2)
        n//=10
    if s>9:
        s=happ(s)
    return s
if happ(n)==1 or happ(n)==7:
    print('True')
else:
    print('False')