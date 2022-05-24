ya = int(input("Please Enter as you wish : "))

if (ya%400 == 0):
    print("%d is a Leap year" %ya)
elif (ya%100 == 0):
    print("%d is Not" %ya)
elif (ya%4 == 0):
    print("%d is a Leap year" %ya)
else:
    print("%d is Not" %ya)
