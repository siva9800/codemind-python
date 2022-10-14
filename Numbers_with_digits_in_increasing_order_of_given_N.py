def printStrictlyInc(n, result='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', prev='0'):
 
    # if the string becomes n–digit, print it
    if n == 0:
        print(result, end=' ')
        return
 
    # start from the next digit (the last digit is `prev`)
    for ch in range(ord(prev) + 1, ord('9') + 1):
        printStrictlyInc(n - 1, result + chr(ch), chr(ch))
# Driver code
n = int(input())
if n==1:
    for i in range(0,10):
        print(i,end=' ')
else:
    printStrictlyInc(n)