def getSecondMostFreq(str) :
 
    NO_OF_CHARS = 256
    count = [0] * NO_OF_CHARS
    
    for i in range(len(str)) :
        count[ord(str[i])] += 1
 
    first, second = 0, 0
    # Traverse through the count[]
    # and find second highest element.
    for i in range(NO_OF_CHARS) :
        # If current element is smaller
        # than first then update both
        # first and second
        if count[i] > count[first] :
            second = first
            first = i
        # If count[i] is in between
        # first and second
        # then update second */
        elif (count[i] > count[second] and
            count[i] != count[first] ) :
                second = i
 
    # return character
    return chr(second)
str=input()
res=getSecondMostFreq(str)
# Driver code
if res != NULL :
    print(res)
else :
    print("-1")
 