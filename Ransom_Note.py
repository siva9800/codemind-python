a=input().split(' ')
one=list(a[0])
two=list(a[1])
c=0
for i in one:
    if i in two:
        c+=1
        two.remove(i)
print(len(one)==c)
        
