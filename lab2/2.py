from math import gcd

class Rational:
    def __init__(self, numerator=2, denominator=4):
        if not denominator:
            raise ZeroDivisionError("Division by Zero")
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Value must be int")
        tmp = gcd(numerator, denominator)
        self.__denominator = denominator // tmp
        self.__numerator = numerator // tmp

    def rat(self):
        return f'{self.__numerator} / {self.__denominator}'

    def fl(self):
        return self.__numerator/self.__denominator
try:
    r = Rational()
    print(r.rat())
    print(r.fl())
except AttributeError:
    print("Wrong arguments")