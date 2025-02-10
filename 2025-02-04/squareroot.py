while True:
    i = float(input("Enter number: "))
    r = 1.0    # Provisional square root

    number_of_iterations = 0
    while round(r*r, 4) != i:   # Loop while not close enough
        r = (r + i/r)/2
        number_of_iterations += 1

    print(f'The square root of {i} is {r}')
    print(f'in {number_of_iterations} iterations')