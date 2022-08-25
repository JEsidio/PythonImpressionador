# Make a program that asks how much you earn per hour and the number of hours worked in the month. Calculate and display your total salary for that month.

hourly_wage = float(input('Enter you hourly wage in U$/h: '))

hours_worked = float(input('Enter the total hours worked in the month: '))

salary = hours_worked * hourly_wage

print(f'\nYour total salary of the month is: U$ {salary} dollars')