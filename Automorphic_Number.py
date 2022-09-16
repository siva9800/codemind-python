n=int(input())
s=n*n
l=len(str(n))
if s%(10**l)==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')