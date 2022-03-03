from manager import Manager
from salesman import Salesman

goods = {
    'soap': 40,
    'sugar': 60,
    'rice': 50,
    'powder': 200,
    'cola': 30,
}

a = Manager('Akmat', 'akmat@gmail.com', '21342', balance=0, goods=goods)
b = Salesman('Valid', 'valid@gmail.com', 'qwerty123', balance=0, boss=a)

b.sell('rice')

# print(a.goods)
print(a.balance)
print(b.balance)