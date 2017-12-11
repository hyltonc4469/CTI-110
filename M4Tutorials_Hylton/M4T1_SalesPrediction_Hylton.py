#  CTI-110
#  M4T1-Sales Prediction
#  Marie Hylton
#  10 November 2017
#


# Get the projected total sales.

total_sales = float(input('Enter the projected sales:'))

#  Calculate the profit as 23 percent of total sales.
annual_profit=total_sales*0.23

#  Display the profit.
print('The profit is $',format(annual_profit,',.2f'))
