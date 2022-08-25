# Write a program that asks for the radius of a circle, calculates and displays its area.
import math

pi = round(math.pi, 2)

radius = float(input('Enter the radius of the circle in meters: '))

area = pi * (pow(radius, 2))

print(f'\nThe area of the circle with {radius} radius is: {area} m²')