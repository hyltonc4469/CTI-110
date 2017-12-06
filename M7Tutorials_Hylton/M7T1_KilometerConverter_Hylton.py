#CTI-110
#M7-T1-Kilometer Converter
#Marie Hylton
#4 December 2017

#This program allows for user to enter a distance in kilometers and the distance
#will be converted into miles.  The user can enter three values before being
#exited from the program.


#Global Constant:
CONVERSION_FACTOR= 0.6214

def main():

    #Prompts user to enter distance in kilometers.
    #Display the distance in miles (value passed as an argument):
    #Conversion is placed in a loop.  Cycles three times.
    
    for x in range(1,4):
        kilometers=float(input("Enter the distance in kilometers: "))
        if kilometers>0:
            show_miles(kilometers)
        else:
            print("Enter a number greater than 0.")
    print("Thank you for using the kilometer converter.  Goodbye.")


#Define show_miles converts kilometers into miles.
def show_miles(kilometers):
    #Calculate Miles:
    miles=kilometers*CONVERSION_FACTOR

    #Display the miles:
    print(kilometers,'kilometers equals',format(miles,',.2f'),'miles.')

main()
