for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for x in a:
        if x % 2 != 0:
            ans += 1
    print(ans//2)