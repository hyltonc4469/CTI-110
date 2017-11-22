#CTI-110
#M5T1-Areas of Rectangles
#Marie Hylton
#22 November 2017

#User inputs the length and width of rectangle1.
#User inputs the length and width of rectangle2.
#Calculate the area of rectangle1.
#Calculate the area of rectangle2.
#Compare the area of both rectangles to find the greatest.
#If area1>area2
    #Display "Rectangle 1 has the greatest area."
#Else if area21>area1
    #Display "Rectangle 2 has the greatest area."
#Else
    #Display "Both rectangles have the same area."


def main():
#Get the Dimensions of rectangle 1.
    length1=int(input('Enter the length of rectangle 1: '))
    width1=int(input('Enter the width of rectangle 1: '))

#Get the dimensions of rectangle 2.
    length2=int(input('Enter the length of rectangle 2: '))
    width2=int(input('Enter the width of rectangle 2: '))

#Calculate the areas of the rectangles.
    area1=length1*width1
    area2=length2*width2

#Determine which has the greater area
    if area1>area2:
        print("Rectangle 1 has the greatest area.")
    elif area1<area2:
        print("Rectangle 2 has the greatest area.")
    else:
        print("Both rectangles have the same area.")
main()    
