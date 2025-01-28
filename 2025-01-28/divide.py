num1 = float(input('Please enter dividend:'))
num2 = float(input('Please enter a divisor:'))

if num2 != 0:
    print(f'{num1}/{num2} = {num1/num2}')
    print('That\'s the answer')
else:
    print('*************************')
    print('* Cannot divide by zero *')
    print('*************************')
print('Program complete')

