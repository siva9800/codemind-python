def bintodec(bina):
    b1=bina
    decimal,i,n=0,0,0
    while(bina!=0):
        d=bina%10
        decimal=decimal+(d*pow(2,i))
        bina//=10
        i+=1
    return(decimal)
n=int(input())
c=bin(n)[2:]
v=[]
for  i in c:
    if i=='0':
        i=1
        v.append(i)
    elif i=='1':
        i=0
        v.append(i)
v1=(''.join([str(i) for i in v]))
print(bintodec(int(v1)))

        