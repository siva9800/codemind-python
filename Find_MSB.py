def power(n):
    if  n==0:
        return False
    while n!=1:
        if n%2==1:
            return False
        n//=2
    return True
def nearp(a):
    while power(a)!=True:
        a-=1
    return a
for i in range(int(input())):
    n=int(input())
    print(nearp(n))
