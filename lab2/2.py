import math
class Rational:
    def __init__(self, numerator=2, denominator=4):
        if (denominator == 0):
            raise ZeroDivisionError("Division by Zero")
        if not (isinstance(numerator,int)) or not (isinstance(denominator, int)):
            raise TypeError("Value must be int")
        self.__denominator = int(denominator / math.gcd(numerator,denominator))
        self.__numerator = int(numerator / math.gcd(numerator,denominator))
    def rat(self):
        return(str(self.__numerator) + '/' + str(self.__denominator))
    def fl(self):
        return(self.__numerator/self.__denominator)
try:
    r = Rational()
    print(r.rat())
    print(r.fl())
except AttributeError:
    print("Wrong arguments")