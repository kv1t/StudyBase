def inc(a):
    return a + 1


def dec(a):
    return a - 1


def main(func):
    flag = True
    for i in range(-10, 11, 1):
        if func(i/2) < 0:
            print(('\x1b[6;30;43m' if flag else '\x1b[6;30;47m') + str(round(float(func(i/2)), 2)) + '\x1b[0m', end=' ')
        else:
            print(('\x1b[6;30;43m' if flag else '\x1b[6;30;47m') + ' ' + (str(round(float(func(i/2)), 2)) if i != 0 else '0.0') + '\x1b[0m', end=' ')
        flag = not flag


print('Значение: ', end=' ')
main(float)
print('\n','Инкримент: ', sep='', end='')
main(inc)
print('\n','Декримент: ', sep='', end='')
main(dec)