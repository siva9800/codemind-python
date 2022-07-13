n=input()
d='0123456789'
l=[int(i) for i in n if i in d]
'''s=0
for i in l:
    i=int(i)
    s=s+i'''
print(sum(l))