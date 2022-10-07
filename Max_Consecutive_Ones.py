n=int(input())
l=list(map(str,input().split('0')))
print(max([i.count('1') for i in l]))