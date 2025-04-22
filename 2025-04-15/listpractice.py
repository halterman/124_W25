
def count_positives1(lst: list[int]) -> int:
    count = 0
    for i in range(len(lst)):
        if lst[i] > 0:
            count += 1
    return count

def count_positives2(lst: list[int]) -> int:
    count = 0
    for elem in lst:
        if elem > 0:
            count += 1
    return count


def make_backwards(lst: list) -> None:
    n = len(lst)
    for i in range(n // 2):
        lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]

def selectsort(lst: list[int]) -> None:
    n = len(lst)
    for i in range(0, n - 1):
        smallest = i
        for j in range(i + 1, n):
            if lst[j] < lst[smallest]:
                smallest = j
        if i != smallest:
            lst[i], lst[smallest] = lst[smallest], lst[i]




print(count_positives1([2, -9, 0, 22, -1, 13]))
print(count_positives2([2, -9, 0, 22, -1, 13]))

a = [2, -9, 0, 22, -1, 13]
print(a)
make_backwards(a)
print(a)

b = [2, -9, 0, 7, 22, -1, 13]
print(b)
make_backwards(b)
print(b)

print('--------------------------')
print('Before sorting a =', a)
selectsort(a)
print('After sorting a =', a)