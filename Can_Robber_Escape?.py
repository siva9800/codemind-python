n=int(input())
l=[int(x) for x in input().split()] 
odd=[i for i in l if i%2!=0]
if len(odd)>2:
    print('NO')
else:
    print('YES')