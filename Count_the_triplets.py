for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    s=sorted(arr)
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if s[i]+s[j] in s:
                c+=1
            elif s[i]+s[j]>s[-1]:
                break
    if c==0:
        print('-1')
    else:
        print(c)