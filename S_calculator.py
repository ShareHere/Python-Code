num1 =int(input("enter a number"))
op =input("enter a operator")
num2 =int(input("enter another number"))

if op =="+":
    print(num1+num2)
elif op =="-":
    print(num1-num2)
elif op =="/":
    print(num1/num2)
elif op =="*":
    print(num1*num2)
else:
    print("invalid operator")
