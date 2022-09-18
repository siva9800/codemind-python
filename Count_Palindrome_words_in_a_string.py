def palin(n):
    i=0
    j=len(n)-1
    while i<j:
        if n[i]!=n[j]:
            return False
        i+=1
        j-=1
    return True
c=0
for i in input().lower().split():
    if palin(i):
        c+=1
print(c)