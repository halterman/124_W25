size = int(input('Enter size of times table: '))

for row in range(1, size + 1):
    for column in range(1, size + 1):
        print(f'{row*column}', end=' ')
    print()