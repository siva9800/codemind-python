n=input().split()
mis=0
mas=0
for i in n:
    mis+=ord(min(i))
    mas+=ord(max(i))
print(abs(mis-mas))