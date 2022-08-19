# Make a Program that asks for the 4 bimonthly grades and shows the average.

grades = 4
total = 0
listGrades = []

for i in range(grades):
    listGrades.append(float(input(f'Enter the {i+1}º grade: ')))

for i in listGrades:
    total += i

average = total / grades


print(f'\nYour average grade is {average}')

