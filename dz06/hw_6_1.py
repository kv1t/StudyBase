""" Задание №1.
функция что-то делает со строкой и для непечатных символов (string.whitespace)
вызывает исключение ValueError
"""
from string import whitespace, printable


class NotPrintableAsciiError(Exception):
    pass


def string_processing(text, *args, **kwargs):
    # блок вашего кода, который преобразовывает строку к новому виду,
    # которое сохроняете в переменной result
    # заменяет whitespace символы на пробелы и непечатные ascii коды на знаки вопроса, удаляет лишние пробелы
    result = ''
    lastChr = ''
    for chr in text:
        try:
            if chr in whitespace:
                raise ValueError()
            elif chr not in printable:
                raise NotPrintableAsciiError('Error')
        except ValueError:
            chr = ' '
        except NotPrintableAsciiError:
            chr = '?'
        if chr == lastChr == ' ':
            pass
        else:
            result += chr
        lastChr = chr
    return result


def main():
    strOne = '''This is example string without whitespaces except spacebars'''
    strTwo = '''Example string
                    with newline and tab whitespaces
                    '''
    strThree = '''Example string with: 
                      newline      ©
                      tab æ
                      someüÂ ascii symbols µµØ¶Š
                    '''
    print(string_processing(strOne))
    print(string_processing(strTwo))
    print(string_processing(strThree))


if __name__ == "__main__":
    main()