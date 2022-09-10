def coun(n):
    n=list(n)
    v='aeiouAEIOU'
    c=0
    i=0
    j=len(n)-1
    for i in range(len(n)//2):
        if (n[i] in v and n[j] not in v) or (n[i] not in v and n[j] in v):
            c+=1
        j-=1
    return c
a=input().split()
c=0
for i in a:
    c+=coun(i)
print(c)