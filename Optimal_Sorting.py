for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=sorted(l)
    if s==l:
        print('0')
    else:
        print(max(l)-min(l))