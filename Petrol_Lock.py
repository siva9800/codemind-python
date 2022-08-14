n=int(input())
l=[int(x) for   x in  input().split()]
s=sum(l)//2
for i in l:
    s=s-i
    if s<=0:
        break
if s==0:
    print('YES')
else:
    print("NO")