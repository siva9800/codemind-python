a=int(input())
ab=list(map(int,input().split()))
c=list(map(int,input().split()))
s=0
if sum(c)>sum(ab):
    print(sum(c)-sum(ab))
else:
    print('0')