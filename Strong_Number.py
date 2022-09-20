def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
t=n
s=0
while n>0:
    r=n%10
    s+=fact(r)
    n//=10
if t==s:
    print("The number {} is a strong number".format(t))
else:
    print('The number {} is not a strong number'.format(t))