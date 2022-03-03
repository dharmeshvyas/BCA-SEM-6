class Product:
    def __init__(self):
        self.__maxprice = 100
        self.__minprice = 1

    def SellingPrice(self):
        print('Our Product maximum price is {}'.format(self.__maxprice))
        print('Our Product minimum price is {}'.format(self.__minprice))

    def productMaxPrice(self, price):
        self.__maxprice = price

    def productMinPrice(self, price):
        self.__minprice = price

prod1 = Product()
prod1.SellingPrice()
prod1.__maxprice = 1500
prod1.SellingPrice()

prod1.__minprice = 15
prod1.SellingPrice()
prod1.productMaxPrice(1500)
prod1.SellingPrice()
prod1.productMinPrice(15)
prod1.SellingPrice()