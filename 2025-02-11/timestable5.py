size = int(input('Enter size of times table: '))

# Print the column titles
print('      ', end='')
for column in range(1, size + 1):
    print(f'{column:4}', end='')
print()

# Print the line under the column titles
print('     +', end='')
for column in range(1, size + 1):
    print('----', end='')
print()

# Print row titles and the body of the table
for row in range(1, size + 1):
    # Print row title
    print(f'{row:4} |', end='')

    # Print the content of the row
    for column in range(1, size + 1):
        print(f'{row*column:4}', end='')
    print()