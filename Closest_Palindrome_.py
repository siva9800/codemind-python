def pali(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n//=10
    return s
def nextpali(n):
    t=n
    n+=1
    while n!=pali(n):
        n+=1
    return n
def beforpalin(n):
    n-=1
    while n!=pali(n):
        n-=1
    return n
n=int(input())
ne=nextpali(n)
be=beforpalin(n)
if (ne-n)==(n-be):
    print(be,ne)
elif ne-n > n-be :
    print(be)
else:
    print(ne)