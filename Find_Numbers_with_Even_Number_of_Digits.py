def count(n):
    c=0
    while n>0:
        r=n%10
        c+=1
        n//=10
    return c%2==0
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if count(i):
        c+=1
print(c)
