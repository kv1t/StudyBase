print('Task 6')
text = 'нет результата'
number = input('Введите целое число от 0 до 5 включительно: ')
if 0 <= int(number) <= 5:
    print(number)
else:
    print("Ошибка " + text)
