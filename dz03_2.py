print('Task 5')
nameStr = input("Как вас зовут?")
ageStr = input("Сколько вам лет?")
cityStr = input("Как называется город, в котором вы живете?")
message = '{0}, возраст {1}, проживающий в г. {2}, далее именуемый заказчиком...'
print(message.format(nameStr,ageStr,cityStr))