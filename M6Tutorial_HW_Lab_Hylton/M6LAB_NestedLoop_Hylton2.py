#CTI-110
#M6LAB-Nested Loop
#Marie Hylton
#27 November 2017

def main():
    import turtle
    play=turtle.Screen()
    play.title("My Nested Loop Snowflake")
    jesse=turtle.Turtle()
    play.bgcolor("skyblue")
    jesse.color("blue")
    jesse.speed(10)
    
    

    #User Input:
    numSides=int(input("How many sides in the polygon?"))
    
    #Initialize Variables
    angle=0
    angle=360/numSides
    n=0
    n=(numSides*2)
    distance=100
    
    
    jesse.left(180)

    for x in range(numSides):
        for i in range(numSides):
            jesse.forward(95)
            jesse.right(angle)
        jesse.forward(95)
        jesse.left(angle)
        jesse.forward(35)
        for i in range(n):
            jesse.forward(30)
            jesse.right(angle)
            jesse.forward(distance)
            jesse.right(angle)
    jesse.forward(25)
    

    play.mainloop()
main()
