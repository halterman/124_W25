
def is_prime(n: int) -> bool:
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes = []
for num in range(2, 100):
    if is_prime(num):
        primes.append(num)
print(primes)

primes2 = [x for x in range(2, 100) if is_prime(x)]
print(primes2)

# primes3 = [is_prime(x) for x in range(2, 100)]
# print(primes3)

pairs = [(x, y) for x in range(4) for y in range(3) if x != y]
print(pairs)


print('------------------------------')

lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
lst2 = ['a', 'b', 'c', 'd',  
        'e', 'f', 'g', 'h']
Z = zip(lst1, lst2)
for t in Z:
    print(t)