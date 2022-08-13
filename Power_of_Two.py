#recursion pow of 2
def t(n):
    if n==1:
        return True
    if n%2!=0 or n==0:
        return False
        
    return (t(n/2))
n=int(input())
if t(n)==True:
    print(True)
else:
    print(False)
