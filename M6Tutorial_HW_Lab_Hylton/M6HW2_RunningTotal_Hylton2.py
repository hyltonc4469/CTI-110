#CTI-110
#M6HW2-Running Total
#Marie Hylton
#29 November 2017
#

#This program uses a loop to calculate the running total of a series of numbers.
#The numbers are inputed by the user.
#Negative numbers are being used as a sentinel to stop the program.

#1.  User will enter a series of numbers.
        #This will need to be a looped user input.
        #User input needs to be displayed in bold text.
        #User input needs to be >=0
#2.  Calculate a running total from these numbers (not necessary to display).
#3.  Sentinel:  input of a negative number.
#4.  Once sentinel is used,
        #Display running total (exclude negative number)
        #Exit program.


def main():
    runningTotal=0
    data=0

    while data>=0:
        data=int(input("Enter a number?"))
        runningTotal+=data
        if data<0:
            print("Total:",runningTotal-data)
        
main()            
