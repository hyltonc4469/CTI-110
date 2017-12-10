#This program allows the user to guess
# a randomly selected number in a guessing game.
#4 December 2017
#CTI-110 M7HW2-Random Number Guessing Game
#Marie Hylton
#

    
    #TAKE OUT "PRINT(NUMBER)" SO NUMBER CAN NOT BE SEEN WHILE PLAYING GAME.





        
import random
number=0
number=random.randint(1, 50)

def main():
    instructions()
    guess=0
    #print(number)       
    for x in range(1):
        guessing_game()
        if guess==number:
            end(guess)
            break
                    

def guessing_game():        
    for x in range(3):
        guess=int(input("Guess the hidden number:"))
        if guess!=number:
            if guess<0 or guess>50:
                print("The range does not precede 0 and does not exceed 50.")
                print("Please guess again.")
            elif guess>=number-1 and guess<=number+1:
                print("You're within one digit!!!")
            elif guess>=number-5 and guess<=number+5:
                print("You're burning up!  You're within 5!!!")
            elif guess>=number-15 and guess<=number+15:
                print("You're warming up!  You're within 15!!!")
            elif number>=25 and guess>=25:
                print("You're warm...kind of.")
            elif number<25 and guess<25:
                print("You're warm...kind of.")
            elif number>=25 and guess<25 or number<25 and guess>25:
                print("Whoa! Stay calm and guess again.")
        elif guess==number:
            end(guess)
            break
        else:
            end(guess)
            break
    while guess!=number:
        reminders_clues()
        last_game(guess)
        break
        

def last_game(guess):
    for x in range(3):
        guess=int(input("Guess the hidden number:"))
        if guess!=number:
            if guess<0 or guess>50:
                print("The range does not precede 0 and does not exceed 50.")
                print("Please guess again.")
            elif guess>=number-1 and guess<=number+1:
                print("You're within one digit!!!")
            elif guess>=number-5 and guess<=number+5:
                 print("You're burning up!  You're within 5!!!")
            elif guess>=number-15 and guess<=number+15:
                print("You're warming up!  You're within 15!!!")
            elif number>=25 and guess>=25:
                print("You're warm...kind of.")
            elif number<25 and guess<25:
                print("You're warm...kind of.")
            elif number>=25 and guess<25 or number<25 and guess>25:
                print("Whoa! Stay calm and guess again.")
        else:
            end(guess)
            break
    
def instructions():
    print("\t\t\tPlay THE GUESSING GAME!")
    print("\t\tThe number is in the range of 1 and 50.")
    print("\tAfter three failed attempts, you can retrieve extra clues!")

    
def reminders_clues():
    print("\t\tRemember:")
    print("\tThe number is in the range of 1 and 49.")
    print("Here are your extra clues:")
    if number%2==0:
        print("\t\tThe hidden number is even.")
    else:
        print("\t\tThe hidden number is odd.")       
    if number>=25:
        print("\t\tThe number is greater than 25.")
    elif number<=25:
        print("\t\tThe number is less than 25.")
        
        
def end(guess):
    if guess==number:
        print("Hooray!  You correctly guessed the hidden number.")
        print("The hidden number is", number,"!")
        print("Goodbye.")
    elif guess!=number:
        print("The hidden number was", number,".")
                    
main()



