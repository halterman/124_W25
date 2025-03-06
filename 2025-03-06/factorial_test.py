def factorial(n: int) -> int:
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


# for i in range(0, 11):
    # print(f'{i:2}: {factorial(i):10}'):w
