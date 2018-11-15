""" Задание №2.
Переделать Задание №1 с созданием и использованием собственное исключение
WhitespaceError с атрибутами:
    position - позиция в строке
    symbol - какой именно непечатный символ
Функция main() демонстрирует работу вашей функции, должна красиво показывать
что именно вызвало исключение.
"""
from string import whitespace, printable


class WhitespaceError(Exception):
    def __init__(self, position, symbol):
        self.position = position
        self.symbol = symbol


class NotPrintableAsciiError(Exception):
    def __init__(self, position, symbol):
        self.position = position
        self.symbol = symbol


def string_processing(text, *args, **kwargs):
    # блок вашего кода, который преобразовывает строку к новому виду,
    # которое сохроняете в переменной result
    """
    Там, где у вас вызывается исключение,
    необходимо сохранить позицию и ошибочный символ в атрибуты исключения
    следующим блоком кода
    вызов_исключения WhitespaceError(ваща_переменна_позиции, ваша_переменная_символа)
    """
    result = ''
    lastChr = ''
    for i, chr in enumerate(text):
        try:
            if chr in whitespace and not chr == ' ':
                raise WhitespaceError(i, chr)
            elif chr not in printable:
                raise NotPrintableAsciiError(i, chr)
        except WhitespaceError as e:
            print('\x1b[1;33mWhitespace symbol {0} found at {1} position\x1b[0m'.format(repr(e.symbol), str(e.position)))
            chr = ' '
        except NotPrintableAsciiError as e:
            print('\x1b[1;31mNot printable ascii symbol {0} found at {1} position\x1b[0m'.format(repr(e.symbol), str(e.position)))
            chr = '?'
        if chr == lastChr == ' ':
            pass
        else:
            result += chr
        lastChr = chr
    return result


def main():
    """
    Вызываете свою функцию с тестовыми данными и красиво сообщаете о том, что произошло
    """
    strOne = '''This is example string without whitespaces except spacebars'''
    strTwo = '''Example \x0bstring\r
                    with \n\x0cnewline and tab\t whitespaces
                    '''
    strThree = '''Example \n\tstring with: 
                      newline, \r     ©
                      tab, æ\x0c
                      someüÂ \x0bascii symbols µµØ¶Š
                    '''
    print(string_processing(strOne), end='\n\n')
    print(string_processing(strTwo), end='\n\n')
    print(string_processing(strThree), end='\n\n')


if __name__ == "__main__":
    main()
    
