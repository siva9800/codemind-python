# An efficient Python program to find bit-wise & of
# all numbers from x to y.
 
# Function to find Bit-wise & of all numbers from x
# to y.
def andOperator(a,b):
     
    # ShiftCount variables counts till which bit every value will convert to 0
    shiftcount=0
     
    # Iterate through every bit of a and b simultaneously
    # If a == b then we know that beyond that the and value will remain constant
    while(a!=b and a>0):
        shiftcount=shiftcount+1
        a=a>>1
        b=b>>1
         
    return a<<shiftcount
a,b=map(int,input().split())
print(andOperator(a, b))