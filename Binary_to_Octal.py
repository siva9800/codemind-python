def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return(decimal) 
for i in range(int(input())):
    a=int(input())
    dec=binaryToDecimal(a)
    octa=oct(dec)
    print(octa[2:])