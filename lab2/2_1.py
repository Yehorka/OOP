class Product:
    def __init__(self, price, description, dimensions):
        self.__price = price
        self.__description = description
        self.__dimensions = dimensions
        if (isinstance(price,str)):
            raise TypeError("Must be numeric")
    def getprice(self):
        return self.__price
    def getdescription(self):
        return self.__description
class Customer:
    def __init__(self, surname, name, patronymic, mobile_phone):
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__mobile_phone = mobile_phone
    def getsurname(self):
        return self.__surname
    def getname(self):
        return self.__name
    def getpatronymic(self):
        return self.__patronymic
class Order:
    def __init__(self, product, customer):
        self.__product_list = []
        self.__customer = customer
        self.__product_list.append(product)
    def display(self):
        for item in self.__product_list:
            print(f'{item.getprice()}')
        print(f'{self.__customer.getname()}')
    def add(self, product):
        self.__product_list.append(product)
    def calc_sum(self):
        sum = 0
        for prod in self.__product_list:
            sum += prod.getprice()
        return sum
p = Product(100, "penis", "large")
c = Customer("Dickens", "Dick", "Dickovich", 390009)
o = Order(p,c)
o.add(Product(120.1, "cunt", "small"))
o.display()
print(f'{o.calc_sum()}')



