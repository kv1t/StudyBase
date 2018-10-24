print('Task 1')
a = 3
b = 4
c = 5
print('Стороны треугольника: ', a, b, c)
p = (a + b + c)/2
area = (p * (p - a) * (p - b) * (p - c))**(1/2)
print('Его площадь равна:', area)

print('Task 2,3')
a = 1
b = 2
print('До изменения: ','a =', a, 'b =', b)
a = a + b
b = a - b
a = a - b
print('После изменения: ','a =', a, 'b =', b)

print('Task 4')
a = input('Введите целое число: ')
if (int(a) % 2):
    print(int(a) * 2)
else:
    print(int(a) ** 2)
