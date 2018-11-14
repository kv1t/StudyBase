def div(firstNum, secondNum):
    if secondNum == 0:
        raise ZeroDivisionError
    else:
        return firstNum / secondNum

def add(firstNum, secondNum):
    return firstNum + secondNum

def sub(firstNum, secondNum):
    return firstNum - secondNum

def mult(firstNum, secondNum):
    return firstNum * secondNum

def sqr(number):
    if number < 0:
        raise Exception
    else:
        return number ** (1/2)

def oneDiv(number):
    if number == 0:
        raise ZeroDivisionError
    else:
        return 1 / number