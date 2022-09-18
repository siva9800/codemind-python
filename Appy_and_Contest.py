def lc(a,b):
    maxi=max(a,b)
    while True:
        if maxi%a==0 and maxi%b==0:
            break
        else:
            maxi+=max(a,b)
    return maxi
for _ in range(int(input())):
    n, a,b,k = map(int, input().split())
    lcm = lc(a,b)
    ans = n//a + n//b - 2*(n//lcm)
    if ans >= k:
        print('Win')
    else:
        print('Lose')