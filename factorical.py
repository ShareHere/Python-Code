num=int(input("enter your number ="))
fac=1
if num<0:
    print("factricol is not exict")
elif num==0:
    print("factorical is to be 1")
else:
    for m in range (1,num+1):
        fac=fac*m
    print("factorical of given"+ str(num) +"is" + str(fac) +"!")
    


