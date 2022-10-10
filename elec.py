import datetime
Units=int(input("Please enter a specific units: "))#current month
if Units<=100:
    current_amount=(Units)*2
    fixed_amount=25
elif 100<Units<=200:
    current_amount=(Units)*3.5
    fixed_amount=50
total_amount=current_amount+fixed_amount
print(total_amount)
bill_date= input(datetime.datetime.strptim('%m/%d/%y'))
if bill_date>=2021-06-21:
    Extra_charge=0.05*(current_amount)
else:
    Extra_charge=0
Finial_bill=total_amount+Extra_charge
print(Finial_bill)    
print("Thanks for calculating Bill!\n Will meet Soon")

