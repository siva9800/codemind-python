for i in range(int(input())):
    n=int(input())
    b=0
    while n>=2**b:
        b+=1
    print((2**(b-1)-1))