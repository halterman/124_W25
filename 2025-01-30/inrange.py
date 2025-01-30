number = int(input('Please enter a number in the range 1 to 5, inclusive: '))

if number >= 1:
    if number <= 5:
        if number == 1:
            print('one')
        elif number == 2:
            print('two')
        elif number == 3:
            print('three')
        elif number == 4:
            print('four')
        elif number == 5:
            print('five')
    else:
        print('Number is too big')
else:
    print('Number is too small')
