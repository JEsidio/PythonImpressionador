# Make a Program that asks for the temperature in degrees Fahrenheit, transforms and displays the temperature in degrees Celsius.
# C = 5/9 * (F-32)

temperature_f = float(input('Enter the temperature in degrees Fahrenheit: '))

temperature_c = round((5 / 9) * (temperature_f - 32), 1)

print(f'\nThe temperature in degrees Celsius is: {temperature_c}ºC')