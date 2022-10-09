n=int(input())
l=list(map(int,input().split()))
profit,mini=0,l[0]
for i in range(1,n):
    mini=min(mini,l[i])
    profit=max(profit,l[i]-mini)
print(profit)