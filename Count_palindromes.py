n=int(input())
m=list(map(int,input().split()))
c=0
def palin(u):
    s=0
    g=u
    while u>0:
        r=u%10
        s=s*10+r
        u=u//10
    if g==s:
        return True
for i in m:
    if palin(i)==True:
        c=c+1
print(c)