#CTI 110
#M5LAB: Debugging
#Marie Hylton
#25 November 2017
#

#Define Letter Grading Scale using 10-point number system.
#User inputs score/number grade.  Assign variable: score
#Base Letter Grade on Grading Scale Guidelines.
#Print Letter Grade for User.

#A=score>=90
#B=80<=score<=89
#C=70<=score<=79
#D=60<=score<=69
#F=score<=59


def main():
    # This program takes a number grade and outputs a letter grade.

    # System uses 10-point grading scale.  Initialize Variables:
    score=0
    A_score=90 
    B_score=80 
    C_score=70
    D_score=60
    F_score=0

    while 1==1:
       
        score = int(input('Enter grade: '))

        if 100>=score>=90:
            print('Your grade is: A')
        elif 89>=score>=80:
            print('Your grade is: B')
        elif 79>=score>=70:
            print('Your grade is: C')
        elif 69>=score>=60:
            print('Your grade is: D')
        else:
            print('Your grade is: F')
    

# program start
main()
