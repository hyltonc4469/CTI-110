#CTI-110
#M5HW2-Software Sales
#Marie Hylton
#22 November 2017
#


#Initialize Variables:
    #package=retail price for one package.
        #package=$99
        #x=number of packages purchased by consumer.
    #discount=percentage marked off, dependent upon # of packages purchased.
        #discount ranges from 0%:40%
    #total_Purchase=total amount due, to include the applied discount (if any)
        #total_Purchase=(x*package)*(discount)

#User inputs the number of packages purchased.
    #User input becomes the variable "x"
#Display the amount of the discount (if any)
    #Discount is based on variable x (user input)

#Calculate whether or not a discount is applied

#If Quantity ranges from 1:9:
    #print "There is no discount applied."
    #print "Your Total Purchase price is: ", total_Purchase
#If Quantity ranges from 10:19:
    #print "There is a 10% discount applied."
    #print "Your Total Purchase price is: ", total_Purchase
#If Quantity ranges from 20:49:
    #print "There is a 20% discount applied."
    #print "Your Total Purchase price is: ", total_Purchase
#If Quantity ranges from 50:99:
    #print "There is a 30% discount applied."
    #print "Your Total Purchase price is: ", total_Purchase
#If Quantity ranges from 100+:
    #print "There is a 40% discount applied."
    #print "Your Total Purchase price is: ", total_Purchase

#Diplay the total purchase cost with the discount applied.


def main():
#Determine the number of packages purchased by the consumer.
    #x=0
    package=99
    #discount=0
    #total_Purchase=(x*package)*(discount)

    
    x=int(input('Enter the number of packages purchased: '))
    if x<=0:
        print("No purchase has been made.")
        print("Please make a purchase.")
    elif 1<=x<=9:
        print("There is no discount applied.")
        discount=0
        discount_Amount=(x*package)*(discount)
        total_Purchase=(x*99)-discount_Amount
        print("Your Total Purchase price is: $",format(total_Purchase,',.2f'))
    elif 10<=x<=19:
        print("There is a 10% discount applied.")
        discount=.10
        discount_Amount=(x*package)*(discount)
        total_Purchase=(x*package)-discount_Amount
        print("Your Total Purchase price is: $",format(total_Purchase,',.2f'))
    elif 20<=x<=49:
        print("There is a 20% discount applied.")
        discount=.20
        discount_Amount=(x*package)*(discount)
        total_Purchase=(x*package)-discount_Amount
        print("Your Total Purchase price is: $",format(total_Purchase,',.2f'))
    elif 50<=x<=99:
        print("There is a 30% discount applied.")
        discount=.30
        discount_Amount=(x*package)*(discount)
        total_Purchase=(x*package)-discount_Amount
        print("Your Total Purchase price is: $",format(total_Purchase,',.2f'))
    else:
        print("There is a 40% discount applied.")
        discount=.40
        discount_Amount=(x*package)*(discount)
        total_Purchase=(x*package)-discount_Amount
        print("Your Total Purchase price is: $",format(total_Purchase,',.2f'))
main()
              




