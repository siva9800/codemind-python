def inttorom(n):
    m=['','M','MM','MMM','MMMM']
    c=['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    t=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    o=['','I','II','III','IV','V','VI','VII','VIII','IX']
    tho=m[(n//1000)]
    hund=c[((n%1000)//100)]
    ten=t[((n%100)//10)]
    on=o[((n%10))]
    ans=(tho+hund+ten+on).replace(' ','')
    return ans
print(inttorom(int(input())))