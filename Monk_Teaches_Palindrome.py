def palindrome(l):
    l1=l[::-1]
    if l1==l and len(l)%2==0:
        return 'YES EVEN'
    elif l1==l and len(l)%2==1:
        return 'YES ODD'
    else:
        return 'NO'
n=int(input())
for i in range(n):
    a=input()
    print(palindrome(a))