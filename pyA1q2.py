#Question2: Prog to compute person's income tax
#All values are in $

gross=float(input("Enter Gross income : "))

std_deduction=10000

dependents=int(input("Enter no. of Dependents : "))
#Deduction allowed for dependent =$3000
dep_deduction=3000

taxable_income = gross-std_deduction-(dependents*dep_deduction)
if(taxable_income<=0):
    print("No Tax")
else:
    print("Taxable Income = ",taxable_income)
    #Given Tax rate = 20% 
    tax = taxable_income*20/100
    print("Tax = ",tax)
    

