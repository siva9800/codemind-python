n=int(input())
maxi='1'*n
dec=int(maxi,2)
for i in range(dec+1):
    c=bin(i)[2::]
    if len(c)==n:
        print(c)
    else:
        while len(c)!=n:
            c=list(c)
            c.insert(0,'0')
        print(''.join(c))