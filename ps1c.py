''''''
# Project: Problem Set 1 - Part C: Finding the right amount to save away
# Date: 4/11/2021
# Description: In the previous versions of this program we were calculating how long it would take
# to be able to afford the down payment on a house based on income, raises, and your selected saving rate.
# What we are trying to calculate here is what the best savings rate to reach the goal within three years.
# We have one input annual_salary.
''''''
#inputs
annual_salary = int(input("Enter your annual salary: "))
#print("Annual Salary: ", annual_salary)
#variable initialization
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
down_payment = total_cost*portion_down_payment
epsilon = 100
investment_return = 0.04
current_savings = 0.0
months = 0
monthly_salary = annual_salary / 12
lower = 0
upper = 10000
step = 0
#we only need to raise enough money for a down payment not the whole cost of the home. hence total_cost*investment_return

