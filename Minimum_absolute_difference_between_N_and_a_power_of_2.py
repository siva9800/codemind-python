n=int(input())
a=0
while 2**a<=n:
    a+=1
print(min(abs(2**a-n),abs(2**(a-1)-n)))
print(b,c)