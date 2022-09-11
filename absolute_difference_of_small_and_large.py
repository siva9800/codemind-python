n=input().split()
for i in n:
    print(abs(ord(min(i))-ord(max(i))),end=' ')