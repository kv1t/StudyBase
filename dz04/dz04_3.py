print('Task 3')
a = int(input('Введите длину треугольника: '))
b = int(input('Введите высоту треугольника: '))
border = a / b
for y in range(b):
    for x in range(a):
        if ((x + 1) / (y + 1)) <= border:
            print('*',end = '')
        else:
            print(' ',end = '')
    print()