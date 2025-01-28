number = int(input('Please enter 1, 2, 3, 4, or 5: '))

if number == 1:
    word = 'one'
elif number == 2:
    word = 'two'
elif number == 3:
    word = 'three'
elif number == 4:
    word = 'four'
elif number == 5:
    word = 'five'
else:
    word = '?????'

print(f'{number} is {word}')