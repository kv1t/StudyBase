print('Task 2')
n = int(input('Введите натуральное число: '))
fact = 1
for i in range(n):
    fact *= (i + 1)
print('факториал числа: ', fact)