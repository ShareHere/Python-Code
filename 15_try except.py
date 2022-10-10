try:
    num_=int(input("enter a number"))
    print("num_")

except:
    print("invaild number")

try:
    answer =10/0
    num_=int(input("enter a number"))
    print("num_")
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invaild number")

