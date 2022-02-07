# 1 DONE
# class Factory:
#     def engine(self):
#         return "Двигатель создать"
#
#     def bridge(self):
#         return "Ходовая часть создана"


# 2
# class Toyota(Factory):
#     def wheels(self):
#         return "Колеса готовы"
#
#     def windows(self):
#         return "Стекла готовы"
#
# a = Toyota()
# list = []
# list.append(a.engine())
# list.append(a.bridge())
# list.append(a.wheels())
# list.append(a.windows())
# print(list)


# 1
class Zoo:
    def __init__(self):
        self.animal_1 = "Тигр"
        self.animal_2 = "Бегемот"
        self.animal_3 = 'Жираф'

    def lev(self):
        self.animal_1 = "Лев"
        self.animal_4 = [self.animal_2, self.animal_3]
        self.animal_3 = "Змея"

    def printer(self):
        print(self.animal_1, self.animal_2, self.animal_3, self.animal_4)

a = Zoo()
a.lev()
a.printer()
