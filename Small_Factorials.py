def fact(n):
    return 1 if (n==0 or n==1) else n*fact(n-1);
for _ in range(int(input())):
    a=int(input())
    print(fact(a))