import math
print('Task 2')
x = input('Введите число x: ')
if -math.pi <= float(x) <= math.pi:
    print('y =', math.cos(float(x)))
else:
    print('y =', float(x))