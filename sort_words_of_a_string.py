n=input().split()
for i in n:
    c=sorted([j for j in i if j.isalpha()])
    k=0
    for d in range(len(i)):
        if i[d].isalpha():
            print(c[k],end='')
            k+=1
        else:
            print(i[d],end='')
    print(end=' ')