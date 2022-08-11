for i in range(int(input())):
    n=input()
    

    scale = 16 ## equals to hexadecimal
    m=(bin(int(n, scale))[2:])
    s=str(m)
    while(len(s)%4!=0):
        s='0'+s
    print(s)