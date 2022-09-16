n=input().split()
v='aeiouAEIOU'
for i in n:
    c=sorted([j for j in i if j not in v])
    k=0
    for d in range(len(i)):
        if i[d] not in v:
            print(c[k],end='')
            k+=1
        else:
            print(i[d],end='')
    print(end=' ')