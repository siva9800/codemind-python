n=int(input())
l=list(map(int,input().split()))
even,odd=0,0
if n%2!=0:
    l.append(0)
for i in range(0,len(l),2):
    even+=l[i]
    odd+=l[i+1]
if abs(even-odd)==0:
    print('YES')
else:
    print('NO')