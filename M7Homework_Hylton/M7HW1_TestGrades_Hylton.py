#Test Average and Grade
#4 December 2017
#CTI-110 M7HW1-Test Average and Grade
#Marie Hylton
#


def main():
    grades,amount=test_grades()
    average(grades,amount)

def test_grades():
    amount=int(input("How many grades do you need to enter: "))
    grades=0
    for x in range(1,amount+1):
        grade=int(input("Enter grade: "))
        grades+=grade
    return(grades,amount)

def average(grades,amount):
    score=(grades/amount)
    print("The average of your",amount,"grades is",score,".")

main()
