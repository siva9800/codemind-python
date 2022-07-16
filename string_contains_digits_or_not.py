n=int(input())
for i in range(n):
    a=input()
    x=[i for i in a if i.isdigit()==True]
    if len(x)==0:
        print('No')
    else:
        print('Yes')