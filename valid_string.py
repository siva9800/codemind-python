a=input()
d=[a.count(i) for i in a if a.count(i)%2==0]
e=[a.count(i) for i in a if a.count(i)%2==1]
if len(d)==len(a):
    print('Valid String')
elif len(e)==1:
    print('Valid String')
else:
    print('Not Valid')