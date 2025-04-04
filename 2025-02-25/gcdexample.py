def gcd(m: int, n: int) -> int:
    # Determine the smaller of m and n
    min = m if m < n else n
    # 1 is definitely a common factor to all ints
    largestFactor = 1
    for i in range(1, min + 1):
        if m % i == 0 and n % i == 0:
            largestFactor = i # Found larger factor
    return largestFactor

# Get an integer from the user
def get_int() -> int:
    return int(input('Please enter an integer: '))

# Main code to execute
def main() -> None:
    n1 = get_int()
    n2 = get_int()
    print(f'gcd({n1}, {n2}) = {gcd(n1, n2)}')

# Run the program
main() 