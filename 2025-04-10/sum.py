def sum(*nums: float) -> float:
    s = 0
    for num in nums:
        s += num
    return s

print(sum(2, 5))
print(sum(2))
print(sum(2, 18, 5))
print(sum(25, 7, 36, 18, 33, 9, 44, 21, 11, 8))
print(sum(2, 5, 89, 22, 6))
print(sum(*(2, 5, 89, 22, 6)))