x,p1,p2,n=map(int,input().split())
xor=((x>>p1)^(x>>p2))&((1<<n)-1)
print(x^((xor<<p1)|(xor<<p2)))