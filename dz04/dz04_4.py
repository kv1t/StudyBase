print('Task 4 равнобедренный треугольник')
a = int(input('Введите длину основания равнобедренного треугольника: '))
b = int(input('Введите длину высоты к основанию равнобедренного треугольника: '))
border = a / (2 * b)
for y in range(b):
    for x in range(a):
        if x > (a/2 - 1):
            if ((x - a/2 + 1) / (y + 1)) <= border:
                print('*',end = '')
            else:
                print(' ',end = '')
        else:
            if ((x + 1) / (b - y)) >= border:
                print('*',end = '')
            else:
                print(' ',end = '')
    print()