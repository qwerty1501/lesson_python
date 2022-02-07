def lesson2():  # DONE
    print("\x1b[4;34mВыполнил: Байбосунов Д.\x1b[0m",
          "Проблема 1 - >=17925",
          "Проблема 2 - 4 Условия",
          "Проблема 3 - Составить любое математическое выражение",
          "Проблема 4 - Что больше",
          "Проблема 5 - -21//10",
          "Проблема 8 - Процент столетия которого Вы прожили",
          "Проблема 9 - Сколько Вам лет 2 года назад и вперед",
          "Проблема 10 - Среднее арифметическое",
          "Проблема 14 - Пять переменных и их выражение",
          "Проблема 17 - Три переменные с точкой",
          sep='\n')
    problem = int(input("Выберите сценарий проблемы: "))
    match problem:
        case (1):
            print("Проблема 1 - >=17925")
            a = (input("Введите число "))
            if (eval(a) >= 17925):
                print(f"Ваше число {eval(a)} больше или равно 17925")
                return again()
            else:
                print(f"Ваше число {eval(a)} меньше чем 17925")
                return again()
        case (2):
            print("1) Число а больше б, но меньше с",
                  "2) Результат деления 7%3*4.8",
                  "3) Два выражения равные друг другу",
                  "4) Два выражения !равные друг другу",
                  sep='\n')
            circs = int(input("Выберите условие: "))
            match circs:
                case (1):
                    a = input("Введите число a: ")
                    b = input("Введите число b: ")
                    c = input("Введите число c: ")
                    if (eval(a) > eval(b) and eval(a) < eval(c)):
                        print("Условие выполнено правильно.")
                        return again()
                    else:
                        print("Условие не выполнено.")
                        return again()
                case (2):
                    print((7 % 3) * 4.8)
                    return again()
                case (3):
                    a = input("Введите число a: ")
                    b = input("Введите число b: ")
                    if (eval(a) == eval(b)):
                        print("Условие выполнено правильно.")
                        return again()
                    else:
                        print("Условие не выполнено.")
                        return again()
                case (4):
                    a = input("Введите число a: ")
                    b = input("Введите число b: ")
                    if (eval(a) != eval(b)):
                        print("Условие выполнено правильно.")
                        return again()
                    else:
                        print("Условие не выполнено.")
                        return again()
                case _:
                    print("\x1b[31mИнвалид\x1b[0m")
                    return again()
        case (3):
            a = input("Введите выражение: ")
            print(f"Ответ: {eval(a)}")
            return again()
        case (4):
            a = input("Введите число a: ")
            b = input("Введите число b: ")
            if (eval(a) > eval(b)):
                print(f"Число a = {eval(a)} больше чем число b = {eval(b)}")
            else:
                print(f"Число a = {eval(a)} меньше чем число b = {eval(b)}")
            return again()
        case (5):
            print(-21 // 10,
                  "\nОтвет является -3 потому что, -21/10 = -2.1 и происходит округление в меньшую сторону, т.е. -3.")
            return again()
        case (8):
            a = int(input("Введите сколько Вам лет: "))
            print(f"Вы прожили {a}% этого столетия")
            return again()
        case (9):
            a = int(input("Введите год Вашего рождения: "))
            # b = int(input("Введите текущий год: "))
            b = 2021
            print(((b - a) - 2), "столько было Вам лет 2 года назад \n", ((b - a) + 2),
                  "столько Вам исполнится через 2 года")
            return again()
        case (10):
            a, b, c, d = map(int, input("Введите 4 числа: ").split())
            z = [a, b, c, d]
            # z = [25, 75, 10, 95]
            print("Среднее арифметическое =", sum(z) / len(z));
            return again()
        case (14):
            print("a) Четное число",
                  "b) Любое от 5 до 15",
                  "c) Дробное число до 20",
                  "d) Любое нечетное число",
                  "e) Любое число",
                  sep='\n')
            while True:
                a = int(input("Введите любое четное число: "))
                if a % 2 != 0:
                    print(f"\x1b[31mВы ввели нечетное число {a}.\x1b[0m")
                else:
                    print(f"\x1b[32mВы ввели четное число {a}\x1b[0m")
                    break
            while True:
                b = int(input("Введите любое число от 5 до 15: "))
                if b < 5 or b > 15:
                    print(f"\x1b[31mВаше число {b} не входит в диапозон от 5 до 15.\x1b[0m")
                else:
                    print(f"\x1b[32mВаше число {b} входит в диапозон от 5 до 15\x1b[0m")
                    break
            while True:
                c = int(input("Введите любое дробное число до 20: "))
                print("Как понимать это условие?")
                break
            while True:
                d = int(input("Введите любое нечетное число: "))
                if d % 2 == 0:
                    print(f"\x1b[31mВы ввели четное число {d}.\x1b[0m")
                else:
                    print(f"\x1b[32mВы ввели нечетное число {d}\x1b[0m")
                    break
            while True:
                e = int(input("Введите любое число: "))
                print(f"\x1b[32mВы ввели число {e}.\x1b[0m")
                break

            print(f"{a}-{e}^({b}/{d}))%{c} = ", ((a - e ** (b / d)) % c))
            return again()
            # var = input("Выберите сценарий: ")
            # match var:
            #       case"a":
            #             while True:
            #                   a = int(input("Введите любое четное число: "))
            #                   if a % 2 != 0:
            #                         print(f"Вы ввели нечетное число {a}.")
            #                   else:
            #                         print(f"Вы ввели четное число {a}")
            #                         return again()
            #       case"b":
            #             while True:
            #                   b = int(input("Введите любое число от 5 до 15: "))
            #                   if b >= 5 and b <= 15:
            #                         print(f"Ваше число {b} входит в диапозон от 5 до 15")
            #                         return again()
            #                   print(f"Ваше число {b} не входит в диапозон от 5 до 15.")
            #       case"c":
            #             print("Как понимать это условие?")
            #             return again()
            #       case"d":
            #             while True:
            #                   d = int(input("Введите любое нечетное число: "))
            #                   if d % 2 == 0:
            #                         print(f"Вы ввели четное число {d}.")
            #                   else:
            #                         print(f"Вы ввели нечетное число {d}")
            #                         return again()
            #       case"e":
            #             e = int(input("Введите любое число: "))
            #             print(f"Вы ввели число {e}.")
            #             return again()
        case (17):
            a = float(input("Введите число с плавающей точкой: "))
            print(f"Вы ввели {a},\n ({a} + {a}) * {a} = ", ((a + a) * a))
            return again()
        case _:
            print("\x1b[31mВведена неправильная цифра\x1b[0m")
            return again()


def again():
    while True:
        again = input("\x1b[6;30;42mВведите '1', чтобы вернуться в начало или '0' чтобы выйти: \x1b[0m")
        if again not in {"1", "0"}:
            print("\x1b[31mВведите правильную цифру\x1b[0m")
        elif again == "0":
            return end()
        elif again == "1":
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            return lesson2()


def end():
    input('\x1b[6;30;41mНажмите ENTER чтобы выйти\x1b[0m')


lesson2()
