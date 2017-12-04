#CTI-110
#M6HW3-Factorial
#Marie Hylton
#29 November 2017
#

#This program will display the factorial of a user-inputted number.
#The notation "n!=n-(n-1)!" is the factorial of a non-negative integer "n".

#1.  Gather input from the user:
    #Datatype must be an non-negative integer "n".
    #n=any on-negative integer
    #User response must be notated with bold feature.
#2.  Calculate the factorial for the integer "n".
    #factorial=(n-(n-1)!
    #use for loop:
    #for n in range(1,n):
    #for x in range(n)
    #print(
    #Include the use of a loop.
#3.  Display the factorial.


def main():
    n=int(input("Enter a non-negative number: "))
    if n>=0:
           print("The factorial of",n,"is:", factorial(n))
    else:
            n=int(input("Enter a non-negative number: "))
    while n>0:
        n=int(input("Enter a non-negative number: "))
        if n>=0:
           print("The factorial of",n,"is:", factorial(n))
    while n<0:
            n=int(input("Enter a non-negative number: "))
        


def factorial(n):
    if n<=0:
       return 1
    else:
        return n*factorial(n-1)


main()
