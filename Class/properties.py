# show a property that can't be negetive value

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Value cannot be zero.")
        self.__price = value


product = Product(50)
# product.price = 1
print(product.price)
