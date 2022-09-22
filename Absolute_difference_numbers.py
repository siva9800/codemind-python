n,m=map(int,input().split())
n=str(n)
print(abs(int(n[:m])-int(n[len(n)-m:])))
