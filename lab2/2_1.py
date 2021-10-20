import phonenumbers

class Product:
    def __init__(self, price, description, dimensions):
        self.__price = price
        self.__description = description
        self.__dimensions = dimensions

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        if isinstance(value,(float,int)):
            raise TypeError("Must be numeric")
        if value<=0:
            raise ValueError("Price must be higher than 0")
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self,desc):
        if not isinstance(desc,str):
            raise TypeError("Must be str value!")
        self.__description = desc

    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, desc):
        if not isinstance(desc, str):
            raise TypeError("Must be str value!")
        self.__dimensions = desc
    def __str__(self) -> str:
        return f'{self.__description} {self.dimensions} {self.__price}'

class Customer:
    def __init__(self, surname, name, patronymic, mobile_phone):
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__mobile_phone = mobile_phone
    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, sur):
        if not isinstance(sur,str):
            raise TypeError("Must be str value!")
        self.__surname = sur
    @property
    def name(self):
        return self.__surname
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Must be str value!")
        self.__name = name
    @property
    def patronymic(self):
        return self.__patronymic
    @patronymic.setter
    def patronymic(self, pat):
        if not isinstance(pat, str):
            raise TypeError("Must be str value!")
        self.__patronymic = pat

    @property
    def mobile_phone(self):
        return self.__mobile_phone
    @mobile_phone.setter
    def mobile_phone(self, mob):
        if not isinstance(mob, int):
            raise TypeError("Must be int value!")
        if not phonenumbers.is_possible_number(phonenumbers.parse(mobile_phone)):
            raise ValueError("Number isn`t valid")
        self.__mobile_phone = mob
    def __str__(self) -> str:
        return f'{self.__name} {self.surname} {self.__patronymic} {self.mobile_phone}'
class Order:
    def __init__(self, customer, *products):
        self.__products = products
        self.__customer = customer
    @property
    def customer(self):
        return self.__customer
    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Must be Customer type")
    @property
    def products (self):
        return self.__products
    @products.setter
    def products (self, products):
        if not isinstance(all(products), Product):
            raise TypeError("Must be Product type")
        self.__products = products
    def add(self, *products):
        if not all(isinstance(i, Product) for i in products):
            raise TypeError("Must be Product type")
        self.__products += products
    @property
    def sum(self):
        return self.calc_sum()
    def calc_sum(self):
        sum = 0
        for i in self.products:
            sum += i.price
        return sum
    def __str__(self) -> str:
        st = ""
        for i in self.__products:
            st += str(i) + "\n"
        return f'{self.__customer}\n {st} Total price: {self.sum}'
p = Product(100, "Shovel", "10 inch")
d = Product(130, "Hoe", "6 inch")
q = Product(120, "Pool", "3 inch")
c = Customer("Dickens", "Dick", "Johns", 38053272822)
o = Order(c, p, q)
#print(c)
print(o)




