# Write a program that asks for 2 integers and one real number. Calculate and show:
# a - the product of twice the first and half of the second.
# b - the sum of triple the first and the third.
# c - the third cubed.

int1 = int(input('Enter the 1º integer number: '))
int2 = int(input('Enter the 2º integer number: '))
real = float(input('Enter one real number: '))

# a
twice_int1 = int1 * 2
half_int2 = int2 / 2
product = twice_int1 * half_int2
print(f'\nA - The product of twice the first and half of the second number is: {product}')

# b
triple_int1 = int1 * 3
sum_b = triple_int1 + real
print(f'B - The sum of triple the first with the third number is: {sum_b}')

# c
real_cube = pow(real, 3)
print(f'C - The third number cubed is: {real_cube}')