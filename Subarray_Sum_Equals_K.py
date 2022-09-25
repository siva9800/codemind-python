# Python3 program for
n,k=map(int,input().split())
arr = list(map(int,input().split()))
res=0
for i in range(n):
	summ = 0		
	for j in range(i, n):
		
		# Calculate required sum
		summ += arr[j]

		# Check if sum is equal to
		# required sum
		if summ == k:
			res += 1

print(res)

# This code is contributed by kavan155gondalia
