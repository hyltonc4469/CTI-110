#CTI 110
#M6T1a-Shapes
#Marie Hylton
#27 November 2017

def main():
    
    import turtle
    play=turtle.Screen()
    play.title("Hello, Professor!")
    jesse=turtle.Turtle()
    play.bgcolor("purple")
    

    #program for creating a square:
    jesse.color("yellow")
    jesse.begin_fill()
    for x in range(4):
        jesse.forward(100)
        jesse.left(90)
    jesse.end_fill()
    jesse.left(90)
    jesse.forward(100)
    
    #program for creating a triangle:
    jesse.color("yellow")
    jesse.begin_fill()
    jesse.penup()
    jesse.forward (20)
    jesse.right(90)
    jesse.pendown()
    for x in range(3):
        jesse.forward(100)
        jesse.left(120)
    jesse.end_fill()
    play.mainloop()
main()


