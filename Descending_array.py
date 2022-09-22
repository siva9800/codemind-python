n=int(input())
l=list(map(int,input().split()))
if l==sorted(l,reverse=True):
    print('yes')
else:
    print('no')