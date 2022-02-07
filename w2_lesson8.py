#NOT DONE
#2
# for i in range(3):
#     with open('users.txt', 'a') as users:
#         l = input("Введите логин: ")
#         p = input("Введите пароль: ")
#         users.write(f"Login : {l}\nPassword : {p}\n")



#3
# with open('w.txt', 'r') as ww:
#     a = ww.read()
#     a.split()
#     key = False
#     for i in a:
#         if i == 'w':
#             print("Да")
#             key = True
#     if key == False:
#         print("Нет")


#4
# t_words = []
# with open('python.txt', 'r') as py:
#     a = (py.read())
#     b = a.split()
#     for i in b:
#         k = 0
#         for ii in i:
#             if ii == 't' or ii == 'T':
#                 k = 1
#         if k == 1:
#             t_words.append(i)
# print(t_words)

#5
# with open('database.txt', 'r') as db:
#     text_dict = {}
#     for line in db:
#         key, value = line.split()
#         text_dict[key] = value
# q1 = int(input("Что вы хотите сделать?\n1. Зарегестрироваться\n2. Войти\n>>>"))
# if q1 == 1:
#     while True:
#         login = input("Введите логин: ")
#         if login in text_dict:
#             print("Данный логин уже существует. Введите логин заного.")
#         else:
#             break
#     while True:
#         password, password_check = input("Введите пароль: "), input("Введите повторно пароль: ")
#         if password_check == password:
#             with open('database.txt', 'a') as db:
#                 db.write(f"\n{login} {password}")
#                 print(f"Логин {login} успешно создан.")
#                 break
#         else:
#             print("Пароли не совпадают. Введите пароль заного.")
# elif q1 == 2:
#     while True:
#         login = input("Введите логин: ")
#         password = input("Введите пароль: ")
#         if text_dict[login] == password:
#             print("Добро пожаловать,", login)
#             break
#         else:
#             print("Неверно введен логин или пароль. Введите данные заного.")