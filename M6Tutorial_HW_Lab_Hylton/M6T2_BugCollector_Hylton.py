#CTI-110
#M6T2-Bug Collector
#Marie Hylton
#29 November 2017
#

#This program will tally the number of bugs collected for 7 days:
    #Initialize the accumulator
    #Set accumulator to 0.
        #Total=0
    #For each of 7 days:
        #Input the number of bugs collected for a day
        #Add bugs collected to the running total.
    #Display the total.
def main():
    total=0

    for x in ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
        print('Enter the bugs collected on', x,':')
        bugs=int(input())
        total=total+bugs

    print("You collected a total of", total, "bugs.")

main()



