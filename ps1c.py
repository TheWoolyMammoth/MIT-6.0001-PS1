''''''
# Project: Problem Set 1 - Part C: Finding the right amount to save away
# Date: 4/11/2021
# Description: In the previous versions of this program we were calculating how long it would take
# to be able to afford the down payment on a house based on income, raises, and your selected saving rate.
# What we are trying to calculate here is what the best savings rate to reach the goal within three years.
# We have one input annual_salary.
#got stuck wound up using https://github.com/tuthang102/MIT-6.0001-Intro-to-CS/blob/master/ps1/ps1c.py to help resolve
''''''

annual_salary = float(input('Enter your starting salary: '))
x = annual_salary
total_cost = 1000000
semi_annual_raise = 0.07
current_savings = 0
portion_down_payment = 0.25 * total_cost
months = 0
low = 0
high = 10000
num_guesses = 0
epsilon = 100

while True:
    guess = (high + low) / 2
    annual_salary=x
    current_savings = 0
    for month in range(0, 36):
        monthly_salary = annual_salary / 12
        current_savings = current_savings + float((monthly_salary * guess) / 10000) + (current_savings * 0.04) / 12
        if month % 6 == 0:
            annual_salary = annual_salary + (annual_salary * semi_annual_raise)
    if abs(current_savings - portion_down_payment) <= epsilon:
        print('Best saving rate: ', '%.2f' % (guess / 100))
        print('Step in binary search: ', num_guesses)
        print("Current Savings: ",'$','%.2f' %current_savings)
        break
    else:
        if abs(current_savings - portion_down_payment) > epsilon and current_savings > portion_down_payment:
            high = guess
        # increase portion_save
        if abs(current_savings - portion_down_payment) > epsilon and current_savings < portion_down_payment:
            low = guess
    if low == high:
        print('It is not possible to achieve the goal within three years.')
        break
    num_guesses+=1