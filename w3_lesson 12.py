# 1 DONE
# l = lambda a, b, c: f"Объем бассеина:  {a * b * c}"
# print(l(2, 3, 4))


# 2
# l = lambda a: f"Осталось до нового года: {365 - a} дней"
# print(l(162))


# 3
# def rec(x):
#     if x > 0:
#         if x % 2 != 0:
#             print(x)
#     rec(x+1)
# print(rec(1))


# 4
# l = {"apple", "banana", "cherry"}
# def popit(a):
#     a.pop()
#     print(a)
# popit(l)
# popit(l)


# 1
# from random import randint
#
# def decorator(func):
#     def wrapper():
#         a = func()
#         a = set(a)
#         a = list(a)
#         return a
#     return wrapper
#
# @decorator
# def gen():
#     list_ = []
#     for i in range(100):
#         i = randint(10, 50)
#         list_.append(i)
#     return list_
#
# print(gen())


# 2
# login = input("Введите логин: ")
# password = input("Введите пароль: ")
#
# def autorization(log, pas):
#     log_ord = []
#     pas_ord = []
#     for i in log:
#         log_ord.append(ord(i))
#     for i in pas:
#         pas_ord.append(ord(i))
#     return log_ord, pas_ord
#
# print(autorization(login, password))


# 3
# list = [1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453]
# for i in list:
#     x = (lambda x: x*1.185)
#     print(x(i))