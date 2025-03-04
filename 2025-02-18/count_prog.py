def count(n: int) -> None:
    for i in range(1, n + 1):
        print(i, end= ' ')
    print()

upper_limit = int(input('Enter top: '))
count(upper_limit)



