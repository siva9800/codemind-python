n=input()
v=[]
for i in n:
    i=i.lower()
    if i!=' ' and n.count(i)==1 and i not in v:
        v.append(i)
print(''.join(sorted(v)))