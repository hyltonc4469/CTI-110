#  CTI-110
#  M4HW2-Tip Tax Total
#  Marie Hylton
#  13 November 2017


#  This program uses user input to calculate tip, tax, and total.

print("Hello!")
print("Please tell me how much your meal was below.")
print("\n")

#This it the set tip amount:
tip=float(.18)

#This is the set sales tax:
tax=float(.07)

#This is input from the user, stating cost of meal:
foodCost=float(input("Enter the cost of your meal: $"))

#This is the calculation of sales tax and sub total-->food cost + sales tax:
print("NC Sales Tax \t\t\t 7%")
salesTax=float(tax*foodCost)
print("Sales Tax\t\t\t",format(salesTax,',.2f'))
subTotal=float(format(foodCost+salesTax,',.2f'))
print("Sub Total\t\t\t",subTotal)

#This is the calculation of tip based on taxsubtotal:
print("Restaurant Gratuity Rate: \t 18%")
tipAmount=float(tip * subTotal)
print("Gratuity\t\t\t",format(tipAmount,',.2f'))

#This is the calculation of total meal cost:
totalCost= float(foodCost+salesTax+tipAmount)
print("Total Cost\t\t\t",format(totalCost,',.2f'))
