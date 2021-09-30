import math
class Rational:
    def __init__(self, numerator=2, denominator=0):
        try:
            if (denominator == 0):
                raise ZeroDivisionError("Division by Zero")
            if not (isinstance(numerator,int)) or not (isinstance(denominator, int)):
                raise TypeError("Value must be int")
            self.__denominator = int(denominator / math.gcd(numerator,denominator))
            self.__numerator = int(numerator / math.gcd(numerator,denominator))
        except (TypeError,ZeroDivisionError):
            print("Error")
    def print_rat(self):
        print(self.__numerator, "/",self.__denominator)
    def print_fl(self):
        print(self.__numerator/self.__denominator)
try:
    r = Rational()
    r.print_rat()
    r.print_fl()
except AttributeError:
    print("Wrong arguments")