n=int(input())
s=list(str(n))
for i in range(len(s)):
    if s[i]=='6':
        s[i]='9'
        break
print(''.join(s))