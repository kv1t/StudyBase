def inc(a):
    return a + 1


def dec(a):
    return a - 1


def main(func):
    for i in range(-10, 10, 1):
        if func(i/2) < 0:
            print(round(float(func(i/2)), 2), end=' ')
        else:
            print('', round(float(func(i/2)), 2), end=' ')


main(inc)
print()
main(dec)
