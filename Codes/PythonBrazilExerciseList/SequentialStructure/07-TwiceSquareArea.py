# Write a program that calculates the area of a square, then displays twice that area to the user.

side = float(input('Enter the side length of the square in meters: '))

area = pow(side, 2)

print(f'\nThe area of the square is: {area} m²')
print(f'\nTwice the area of the square is: {area * 2} m²')