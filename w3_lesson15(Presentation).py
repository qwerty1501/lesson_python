class Human:
    default_name = None
    default_age = 0

    def __init__(self, name = default_name, age = default_age):
        self.age = age
        self.name = name
        self.__money = 1000
        self.__house = None

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Бабки: {self.__money}")
        print(f"Дом: {self.__house}")

    @staticmethod
    def default_info():
        print(f"Default name: {Human.default_name}")
        print(f"Default age: {Human.default_age}")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, salary):
        self.__money = self.__money + salary
        print(f"Текущее состояние оценивается в: {self.__money}")

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if price > self.__money:
            print("Недостаточно денег для покупки дома.")
        elif price < self.__money:
            self.__make_deal(house, price)

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f"Финальная стоимость дома составляет: {final_price}")
        return final_price


class SmallHouse(House):
    default_area = 40
    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


if __name__ == '__main__':

    Human.default_info()
    dastan = Human('Дастан', 10)
    dastan.info()

    small_house = SmallHouse(1100)
    dastan.buy_house(small_house, 5)

    dastan.earn_money(100)
    dastan.buy_house(small_house, 5)
    dastan.info()
    a = 0