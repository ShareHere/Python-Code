min_age=1
max_age=21

for i in range (1,4):
    gusses_age=int((max_age+min_age)/2)
    result=input("you are "+ str(gusses_age)+ " old!")
    if result=="correct":
        print("you are correct")
        break
    elif result=="more":
        min_age=gusses_age
    elif result=="less":
        max_age=gusses_age
    else:
        print("error,gusses again")