for i in range(int(input())):
    n=int(input())
    if n%2==0:
        if n%4==0:
            b=3^n
        else:
            b=3
    else:
        if (n-1)%4==0:
            b=(3^n-1) and n
        else:
            b=3
    print(b)