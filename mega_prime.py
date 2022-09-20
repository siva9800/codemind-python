def prime(n):
    if n==1:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
n=int(input())
flag=True
if prime(n)==False:
    print('Not Mega Prime')
else:
    while n>0:
        r=n%10
        if prime(r)==False:
            flag=False
            break
        n//=10
    if  flag==True:
        print('Mega Prime')
    else:
        print('Not Mega Prime')