def subArraySum(arr, n, sum_):

	# Initialize currentSum as
	# value of first element
	# and starting point as 0
	currentSum = arr[0]
	start = 0

	# Add elements one by
	# one to currentSum and
	# if the currentSum exceeds
	# the sum, then remove
	# starting element
	i = 1
	while i <= n:

		# If currentSum exceeds
		# the sum, then remove
		# the starting elements
		while currentSum > sum_ and start < i-1:

			currentSum = currentSum - arr[start]
			start += 1

		# If currentSum becomes
		# equal to sum, then
		# return true
		if currentSum == sum_:
		    return(start+1, i)

		# Add this element
		# to currentSum
		if i < n:
			currentSum = currentSum + arr[i]
		i += 1

	# If we reach here,
	# then no subarray
	return False
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    c=(subArraySum(l, n,k))
    if c==False:
        print('-1')
    else:
        print(*c)