n=input()
l=list(n)
v='AEIOUaeiou'
em=[]
j=0
for i in range(len(l)):
    if l[i] in v:
        em.append(i)
cm=em[::-1]
for i in range(len(em)):
    l[em[i]]=n[cm[j]]
    j+=1
print(''.join(l))