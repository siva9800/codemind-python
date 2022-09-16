n=input()
n=n.lower()
s=set(n)
c=sorted(list(s))
if c.count(' ')>=1:
    v=c.index(' ')
    c.pop(v)
print(''.join(c))