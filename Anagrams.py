s1=input().lower()
s2=input().lower()
if len(s1)!=len(s2):
    print('False')
else:
    d1={i:s1.count(i) for i in s1}
    d2={i:s2.count(i) for i in s2}
print(d1==d2)