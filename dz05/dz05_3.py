def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def div(a, b):
    if b != 0:
        return a / b
    else:
        return 'error, division by 0'


def main():
    while True:
        operation = input('Введите операцию -, +, *, /  для выхода из программы введите exit: ')
        if operation.lower() == 'exit':
            break
        elif operation != '-' and operation != '+' and operation != '*' and operation != '/':
            print('Некорректная операция')
            continue
        a = float(input('Введите a: '))
        b = float(input('Введите b: '))
        if operation == '-':
            print(sub(a, b))
        if operation == '+':
            print(add(a, b))
        if operation == '*':
            print(multiply(a, b))
        if operation == '/':
            print(div(a, b))


main()