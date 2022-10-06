def DistarrayoddSum(m,n):
    c=(n-m)+1
    co=0
    v=[0]*c
    for i in range(c):
        v[i]=m
        m+=1
    for i in range(c):
        if v[i]%2!=0:
            co+=1
        for j in range(i,c):
            s=v[i]+v[j]
            if s%2!=0:
                co+=1
    return co
m=int(input())
n=int(input())
print(DistarrayoddSum(m,n))
            