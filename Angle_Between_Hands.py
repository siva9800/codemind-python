h,m=map(int,input().split(':'))
ans=abs((h*30 + m*0.5)-(m*6))
print(min( 360-ans,ans))