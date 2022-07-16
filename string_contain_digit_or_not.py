a=input()
d=[i for i in a if i.isdigit()==True]
if len(d)==0:
    print("Doesn't contain digit")
else:
    print("Contains {} digit".format(len(d)))