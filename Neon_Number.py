n=int(input())
s=n**n
r=0
if s%9==0:
    r=9
else:
    r=(s%9)
if n==r:
    print("Neon Number")
else:
    print("Not Neon Number")