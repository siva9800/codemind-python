for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=sorted(l)
    st=1
    en=n-1
    t=0
    v=[0]*n
    while st<n:
        v[st]=s[t]
        v[st-1]=s[en]
        st+=2
        en-=1
        t+=1
    if n%2!=0:
        v[-1]=s[en]
    print(*v)