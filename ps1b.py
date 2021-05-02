''''''
# Project: Problem Set 1 - Part B: Saving with a raise
# Date: 4/11/2021
# Description: Building a program that lets you estimate how long it would take for you to buy
# your dream house. the inputs the user provides is annual_salary, portion_saved (decimal)
# total_cost of house, and your semi_annual_raise (decimal). a few preset values portion_down_payment = 0.25 (25%),
# and investment_return = 0.4.
''''''
#inputs
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to be saved each month, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the Semi Annual Raise, as a decimal: "))
#print(annual_salary,portion_saved,total_cost) #testing the inputs
#print(semi_annual_raise) #testing the new input
#variable initialization
portion_down_payment = 0.25
investment_return = 0.04
current_savings = 0.0
months = 0
# i moved monthly salary outside of the loop because it was causing the monthly income to reset to its non-raise value
monthly_salary = annual_salary / 12
#we only need to raise enough money for a down payment not the whole cost of the home. hence total_cost*investment_return
while current_savings < (total_cost*portion_down_payment):
    monthly_return = ((current_savings * investment_return) / 12)
    # print(monthly_salary) #test value
    if months % 6 == 0 and months != 0: #0%6==0 and who gets a raise before they start a job or in the first month?
        salary_raise = (monthly_salary*semi_annual_raise)
        monthly_salary += salary_raise
        # print(monthly_salary) #test value
    current_savings += (monthly_salary * portion_saved) + monthly_return
    months += 1
print("Number of months:",months)
