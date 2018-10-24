print('Task 4')
a = input('Введите первое число: ')
b = input('Введите второе число: ')
if float(a) > float(b):
    print("Первое число больше второго:", float(a) - float(b))
elif float(a) < float(b):
    print("Второе число больше первого:", float(a) + float(b))
else:
    print("Числа равны:", float (a))