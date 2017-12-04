#CTI-110
#M6HW1-Distance Traveled
#Marie Hylton
#29 November 2017
#


#This program displays a table of the distance that a vehicle has traveled/hr.
#Distance=speed*time
#Initialize Variables for speed and time.
#Gather user input:
    #Speed of the vehicle
    #Number of hours traveled
    #Identify user input as variables
#Print heading title for the table
#Create a loop, allowing time to be the changing variable
    #Time needs begin at one and calculate distance traveled up to the user input.
#Display the time and distance traveled by the vehicle.

def main():
    speed=0
    time=0
    speed=int(input('What is the speed of the vehicle in mph?'))
    time=int(input('How many hours has it traveled?'))
    print("Hour\t\t\tDistance Traveled")
    for time in range(1,time+1):
        distance=speed*time
        print (time,"\t\t\t",distance)


main()
