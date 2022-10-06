n=int(input())
l=list(map(int,input().split()))
x,y=0,0
for i in range(1,len(l),2):
    x+=l[i-1]
    y+=l[i]
if (abs(x-y)%4==0):
    print('X')
else:
    print('Y')