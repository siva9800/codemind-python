n=int(input())
m=list(map(int,input().split()))
c=0
def rev(u):
    s=0
    while u>0:
        r=u%10
        s=s*10+r
        u=u//10
    return s
for i in m:
    print(rev(i),end=' ')