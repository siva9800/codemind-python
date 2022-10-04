for _ in range(int(input())):
    a=int(input())
    s=list(str(a))
    v=sorted([int(i) for i in s])
    for i in range(1,len(v)):
        if abs(v[i-1]-v[i])!=1:
            print('NO')
            break
    else:
        print('YES')