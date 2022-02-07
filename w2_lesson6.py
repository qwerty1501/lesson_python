#1  DONE
# lang1 = 'Rust'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if lang1 == i:
#         print("This lang is in list")
#     else:
#         pass


#2
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i != 'php':
#         print(i)
#     else:
#         break


#3
# n = 0
# i = 7
# while n < 5:
#     i = i * i
#     print(i)
#     n = n + 1

#4
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# g = -1
# for i in languages:
#     g = g + 1
#     print(g, i)

# 5
# n = 0
# key = 0
# string = ''
# while key != 2:
#     if n < 10 and key == 0:
#         n += 1
#         string += (str(n)) + ','
#         if n == 10:
#             key = 1
#     elif n > 1 and key == 1:
#         n -= 1
#         string += str(n)
#         if n != 1:
#             string += ','
#     else:
#         key = 2
# print(string)


# #6
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан')
# n = -1
# for i in names:
#     n += 1
#     if n % 2 == 0 and n != 0:
#         print(i)


#7
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан')
# n = 0
# for i in names:
#     n += 1
#     if n % 2 == 0:
#         print(i)
#
#8
# i = int(input("Введите число: "))
# if i > 99 and i < 1000:
#     print("Число трехзначное")
# if i > 0 and i % 2 == 0:
#     print("Число больше 0 и четное")
# if i % 31 == 0:
#     print("Число делится на 31 без остатка")
# if i > 100 and i % 17 == 0 or i > 150 and i == 13**2:
#     print("Если это число больше 100 и оно делится на 17 без остатка или это число больше 150 и равно 13**2. Само число: ", i)

# #9
# numbers = list(range(-100, 100))
# n = 0
# c1 = 0
# c2 = 0
# for i in numbers:
#     n += 1
#     if i % 13 == 0:
#         i *= i
#         if i % 2 == 0:
#             print(i, "делиться на 13 без остатка возводить в квадрат если оно чётное")
#             c1 += 1
#     if n % 7 == 0:
#         if i % 2 != 0:
#             print(i, "- данное каждое 7 число и оно нечетное.")
#             c2 += 1
# print(f"Вошли в 1 условие: {c1}\nВошли во 2 условие: {c2}")
