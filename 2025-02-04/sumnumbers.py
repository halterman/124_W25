# This program sums a sequence of non-negative
# integers the user provides.
# The user terminates the sequence with any 
# negative integer.

sum = 0
print('Enter non-negative integers (negative ends list)')
number = 0
while number >= 0:
    number = int(input('=> '))
    if number > 0:
        sum += number

print(f'The sum is {sum}')