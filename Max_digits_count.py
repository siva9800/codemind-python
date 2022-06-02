n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if i<0:
        i=-i
    c.append(len(str(i)))
print(c.count(max(c)))