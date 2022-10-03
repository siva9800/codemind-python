for _ in range(int(input())):
    n,k=map(int,input().split())
    c=0
    for i in range(n):
        l=list(map(str,input().split()))
        thi=[i for i in range(n) if l[i]=='T']
        poli=[i for i in range(n) if l[i]=='P']
        l,r,res=0,0,0
        while l<len(thi) and r<len(poli):
            if abs(thi[l]-poli[r])<=k:
                res+=1
                l+=1
                r+=1
            elif thi[l]<poli[r]:
                l+=1
            else:
                r+=1
        c+=res
    print(c)