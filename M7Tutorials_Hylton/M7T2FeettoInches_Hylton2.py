#Program Converts Feet to Inches. Performs program three times, then exits.
#4 December 2017
#CTI-110 M7T2_FeettoInches
#Marie Hylton
#

#GLOBAL CONSTANT FOR THE NUMBER OF INCHES PER FOOT.
INCHES_PER_FOOT=12

#MAIN FUNCTION--WILL RUN THREE TIMES, THEN EXITS PROGRAM
def main():
    #GET A NUMBER OF FEET FROM THE USER:
    for x in range(1,4):
        feet=float(input("Enter the measurement in units of feet: "))
        if feet>0:
            #CONVERT USER INPUT(FEET) INTO INCHES:
            print(feet, 'equals', format(feet_to_inches(feet),',.1f'), 'inches.')
        else:
            print("Enter a number greater than 0.")
    print("Thank you for using the Feet to Inches Converter.  Goodbye.")

#THE feet_to_inches FUNCTION CONVERTS FEET TO INCHES.   
def feet_to_inches(feet):
    return feet*INCHES_PER_FOOT    
    
main()
