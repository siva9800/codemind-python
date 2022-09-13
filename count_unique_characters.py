n=input()
c=0
for i in n:
    i=i.lower()
    if i!=' ' and n.count(i)==1:
        c+=1
print(c)