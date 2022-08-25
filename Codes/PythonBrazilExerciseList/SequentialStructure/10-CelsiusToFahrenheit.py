# Make a Program that asks for the temperature in degrees Celsius, transforms and displays it in degrees Fahrenheit.
# F = 9/5 * C + 32

temperature_c = float(input('Enter the temperature in degrees Celsius: '))

temperature_f = round(9/5 * temperature_c + 32, 1)

print(f'\nThe temperature in degrees Fahrenheit is: {temperature_f}ºF')