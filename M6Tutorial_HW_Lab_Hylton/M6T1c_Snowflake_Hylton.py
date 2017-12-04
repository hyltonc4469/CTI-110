#CTI-110
#M6T1c-Snowflake
#Marie Hylton
#27 November 2017

def main():
    import turtle
    play=turtle.Screen()
    play.title("My Snowflake")
    jesse=turtle.Turtle()
    play.bgcolor("skyblue")
    jesse.color("blue")
    jesse.speed(10)

    #Snowflake made from multiple polygons


    
    #Initialize Variables for "n-sided" polygon
    #Create variable from user-input

    print("Enter the number of sides you wish on your snowflake below. (Suggestion: 4)")
    numSides=int(input("How many sides in the polygon?"))
    angle=360/numSides
    sides=range(numSides)
    distance=95
   


    #Create n-sided polygon
    #Nest Loop for additional polygon to add "flakes" to n-sided polygon.

    for i in sides:
        jesse.forward(distance)
        jesse.left(angle)
        for x in range(12):
            for x in range(3):
                jesse.forward(95)
                jesse.right(30)
            jesse.right(120)
    
    play.mainloop()
main()
