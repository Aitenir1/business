from person import Person


class Manager(Person):

    def __init__(self, name, email, password, goods, balance=0):
        super().__init__(name, email, password)
        self.balance = balance
        self.goods = goods

    @classmethod
    def validate_balance(cls, balance):
        if type(balance) not in (int, float):
            raise TypeError('Balance must be a numerical value')

    @classmethod
    def validate_goods(cls, goods):
        if type(goods) != dict:
            raise Exception('Goods must be a dictionary type')

        for good, price in goods.items():
            if type(good) != str or type(price) not in (int, float):
                raise Exception('Goods must be a dictionary with string key - product and number value - price')

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.validate_balance(balance)
        self.__balance = balance

    @property
    def goods(self):
        return self.__goods

    @goods.setter
    def goods(self, goods):
        self.validate_goods(goods)
        self.__goods = goods

    def buy_new(self, product: str, price: int):
        if type(product) != str:
            raise TypeError('The product type must be string')

        if type(price) not in (int, float):
            raise TypeError('The type of a price cannot be non-integer')

        self.goods[product] = price


