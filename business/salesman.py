from person import Person
from manager import Manager


class Salesman(Person):

    def __init__(self, name: str, email: str, password: str, balance: int, boss: Manager):
        super().__init__(name, email, password)
        self.boss = boss
        self.balance = balance

    @classmethod
    def validate_boss(cls, boss):
        if type(boss) != Manager:
            raise Exception('Invalid value for boss attribute')

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, boss):
        self.validate_boss(boss)
        self.__boss = boss

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.boss.validate_balance(balance)
        self.__balance = balance

    def sell(self, product):
        if product not in self.boss.goods.keys():
            raise Exception(f'There is no {product} in assortment')

        price = self.boss.goods[product]
        self.balance += price * 0.1
        self.boss.balance += price * 0.9

        del self.boss.goods[product]
