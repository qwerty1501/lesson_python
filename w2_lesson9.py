# Problem 1  DONE
# import my_module
# tttt

# Problem 2
# from random import choice
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# n = []
# for i in range(4):
#     i = choice(names)
#     names.remove(i)
#     n.append(i)
# print(n)


# Problem 3
# from sys import platform

# print(platform)


# # Problem 4
#
# i = input("a: ")
# ii = input("b: ")
# iii = input("c: ")
# print(i, ii, iii)


# Problem 5
# import os
# # filepath = os.path.join("D:")
# filepath = os.path.join("C:\Users\USER\Desktop")
# my_file = open(filepath, "DEEEK")

# Problem 6
# from random import choice
# teams = []
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# l = len(names)
# for n in range(4):
#     t = []
#     for i in range(l // 4):
#         i = choice(names)
#         names.remove(i)
#         t.append(i)
#     if n == 3 and l / 4 != 0:
#         t.append(names[0])
#     teams.append(t)
# print(teams)

# 1
# sys.argv


# 2
# import sys
# a, b = input("Текст а: "), input("Текст b: ")
# if sys.getsizeof(a) > sys.getsizeof(b):
#     print("Размер a больше чем b")
# else:
#     print("Размер b больше чем a")


# 3
# import string
# from random import choice
# number = int(input("Число символов: "))
# def randompassword(a):
#     chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
#     return ''.join(choice(chars) for x in range(a))
#
# print(randompassword(number))


# 1
# from random import randrange
# print(randrange(6, 12, 2))
# print(randrange(5, 100, 5))


# 2
# import os
# import sys
# print(os.name, os.getlogin(), sys.executable, sys.platform, sep='\n')


# 3
# import datetime
# today = datetime.datetime.now().date()
# print(today + datetime.timedelta(days=1000))
