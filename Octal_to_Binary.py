for i in range(int(input())):
    onum = input()
    bnum = int(onum, 8)
    bnum = bin(bnum)
    print(bnum[2:])