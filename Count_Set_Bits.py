for i in range(int(input())):
    x = int(input())
    y = bin(x)
    c = 0
    for i in y:
        if i=="1":
            c = c+1
    print(c)