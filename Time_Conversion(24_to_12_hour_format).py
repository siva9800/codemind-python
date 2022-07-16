t1=input()
import time
t = time.strptime(t1, "%H:%M")
#timevalue_12hour
print(time.strftime( "%I:%M %p", t ))