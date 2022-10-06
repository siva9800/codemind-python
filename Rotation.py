for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    k=k%n
    for i in range(k):
        a=l.pop()
        l.insert(0,a)
    print(*l)