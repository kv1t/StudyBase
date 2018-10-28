print('Task 1')
a = int(input('Enter a: '))
b = int(input('Enter b(b > a): '))
sum = 0
for i in range(a, b + 1):
    sum += i
print('Sum:',sum)