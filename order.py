# Create a class called Order which stores item & its price. Use Dunder function (__gt__) to convey that:
# order1 > order2 if price of order1 > price of order2

class Order:

    def __init__(self, item, price):
        self.item=item
        self.price=price

    def __gt__(self, o2):
        return self.price> o2.price

item=str(input("Name of an item:- "))
price=int(input("Price:- "))
o1=Order(item, price)

item=str(input("Name of an item:- "))
price=int(input("Price:- "))
o2=Order(item,price)

print(o1>o2)