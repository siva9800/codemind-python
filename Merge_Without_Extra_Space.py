for _ in range(int(input())):
    a,b=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    s=sorted(l1+l2)
    print(*s)