#1 DONE
# def add(a, b):
#     print(a + b)
# def substract(a, b):
#     print(a - b)
# def multiply(a, b):
#     print(a * b)
# def divide(a, b):
#     print(a / b)
#
# add(2, 2)
# substract(2, 2)
# multiply(2, 2)
# divide(2, 2)


#2
# def sent(dick):
#     b = 0
#     for i in dick:
#         b += 1
#     print(b)
#
# sent('Пуля - дура, а дура - не пуля')


#3
# def dicts(a1, a2):
#     print(a1 | a2)
# dict1 = {'one': 1}
# dict2 = {'two': 2}
# dicts(dict1, dict2)


#4
# def delivery(a1, a2):
#     i = open("order.txt", "w+")
#     i.write(a1)
#     i.write(f"\n{a2}")
#     i.close()
# a = input("Введите что хотите покушать: ")
# b = input("Введите что хотите выпить: ")
# delivery(a, b)


#5
# name = input("Введите название файла: ")
# def create_file(name):
#     i = open(name, "w+")
# create_file(name)


#1
# def main():
#     print("I AM MAIN!")
#     not_main()
#
# def not_main():
#     print("I AM NOT =(")
#
# main()


#2
# def dictionary(**double_tuple):
#     tupl1 = double_tuple["values"]
#     tupl2 = double_tuple["keys"]
#     print(tuple(tupl1))
#     print(tuple(tupl2))
# dict = {'One' : 1, 'Two' : 2, 'Dick' : '8==э'}
# dictionary(values = dict.values(), keys=dict.keys())


#3
# def test(a):
#     if a / a == 1 and a / 1 == a:
#         print("Это простое число")
#     else:
#         print("Это не простое число")
# i = int(input("Введите что-то: "))
# test(i)


#1
# def argument(a, b):
#     print(list(a) + list(b))
# argument([1,2,3], (1,2,3))


#2
# def shit(a):
#     b = ''
#     for i in range(a):
#         b += str(a)
#     print(b)
# shit(7)


#3
# def salary(**sal):
#     name = sal["values"]
#     pay = sal["keys"]
#     print(f"{set(name)} - {set(pay)}")
# a = input("Введите ваше имя: ")
# b = input("Введите вашу зарплату: ")
# if b == 0:
#     b = 5000
# print(b)
# c = {a:b}
# salary(values=c.values(), keys=c.keys())

#4
# from random import randint
# def genN(n):
#     n_ = []
#     for i in range(n):
#         n_.append(randint(1, 1000))
#     return n_
# print(genN(5))