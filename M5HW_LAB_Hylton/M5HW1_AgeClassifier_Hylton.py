#CTI-110
#M5HW1-Age Classifier
#Marie Hylton
#22 November 2017
#


#User inputs age of a given person.
#Determine appropriate age classification.

#Base age classification on guidelines:
#If age<=1
    #Display "He/She is an infant."
#If age 2:12
    #Display "He/She is a child."
#If age 13:19
    #Display "He/She is a teenager."
#If age>=20
    #Display "He/She is an adult."



def main():
    age=0
#Ask the user to enter the person's age.
    while 1==1:
        age=float(input('Enter the age of the person: '))
    #Determine the age classification of the person.
        if age<=1.0:
            print("He/She is an infant.")
        elif 1.0<age<13.0:
            print("He/She is a child.")
        elif 13.0<=age<20.0:
            print("He/She is a teenager.")
        else: 
            print("He/She is an adult.")
main()
        
    
    

