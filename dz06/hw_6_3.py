""" Задание №3.
Создать функцию, которая анализирует параметры и если хотя-бы один из них
другого типа, то вызывает исключение (на выбор - одно из стандартных или своё
собственное по примеру Задания №2).
В комментарии обосновать свой выбор.

В функции main() независиимо от того было исключение или не было,
всё-равно надо сообщить с какими аргументами вы вызывали свою функцию и
какого типа был каждый аргумент.
"""
class NotMainValueError(Exception):
    # вызываю свое исключение потому что:
    #  1) сообщаю дополнительные параметры исключению.
    #  2) исключение действует как часть программной логики
    def __init__(self, value, type, maintype):
        self.value = value
        self.type = type
        self.maintype = maintype


def check_params_type(*args, **kwargs):
    typelist = [type(x).__name__ for x in args]
    expdict = dict((x, typelist.count(x)) for x in set(typelist))
    max = 0
    for x in expdict.keys():
        if expdict[x] > max:
            max = expdict[x]
            maintype = x
    for x, i in zip(typelist,args):
        try:
            if x != maintype:
                raise NotMainValueError(i, x, maintype)
        except NotMainValueError as e:
            print('\x1b[1;33mElement {0}, type {1} are different then most other elements type {2}\x1b[0m'.format(e.value, e.type, e.maintype))
    return zip(args, typelist)


def main():
    """
    Вызываете свою функцию с тестовыми данными и красиво сообщаете о том, что произошло
    """
    listOne = [1, 2, 3, 4, 'plane', 3.11, 7, 99, 23, True, 1]
    listTwo = ['a', 'b', 'c', 'd', 'sheep']
    listThree = [.06, 7, 8, .07, .09, 124.0, 11, 9]

    print('Analyze the first list:')
    print(*check_params_type(*listOne))
    print('\nAnalyze the second list:')
    print(*check_params_type(*listTwo))
    print('\nAnalyze the third list:')
    print(*check_params_type(*listThree))


if __name__ == "__main__":
    main()
