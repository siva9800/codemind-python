n=int(input())
m=list(map(int,input().split()))
c=0
def dig(u):
    s=0
    while u>0:
        r=u%10
        s=s+r
        u=u//10
    return s
for i in m:
    c=c+dig(i)
print(c)