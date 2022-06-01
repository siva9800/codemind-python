n=int(input())
m=list(map(int,input().split()))
for i in m:
    if i<0:
        i=-i
    print(len(str(i)),end=' ')