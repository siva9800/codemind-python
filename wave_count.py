def check(n,l):
    amplitude=l[0]-l[1]
    for i in range(1,n-1):
        if l[i]>l[i-1] and l[i+1]<l[i] or l[i]<l[i-1] and l[i+1]>l[i]:
            amplitude=max(amplitude,abs(l[i]-l[i+1]))
        else:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
wave=(n-1)//2
if check(n,l):
    print(wave)
else:
    print('-1')