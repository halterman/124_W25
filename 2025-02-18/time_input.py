from time import time

print('Enter an number:', end= ' ')
start = time()
number = int(input())
stop = time()

print(f'It took you {stop - start} second to respond')
