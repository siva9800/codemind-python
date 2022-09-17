def lcm(a,b):
    if a>b:
        g=a
    else:
        g=b
    while True:
        if g%a==0  and g%b==0:
            lcm=g
            break
        g+=1
    return lcm
n=int(input())
arr=[int(x) for x in input().split()]
ans=lcm(arr[0],arr[1])
for i in range(2,len(arr)):
    ans=lcm(ans,arr[i])
print(ans)