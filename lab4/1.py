from math import gcd

class Rational:
    def __init__(self, numerator=2, denominator=4):
        tmp = gcd(numerator, denominator)
        self.__denominator = denominator // tmp
        self.numerator = numerator // tmp
    @property
    def numerator(self):
        return self.__numerator
    @numerator.setter
    def numerator(self, value):
        if not isinstance(value, int):
            raise TypeError("Value must be int")
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        if not isinstance(value, int):
            raise TypeError("Value must be int")
        if not value:
            raise ZeroDivisionError("Division by Zero")
        self.__denominator = value

    def __str__(self) -> str:
        return f'{self.numerator}/{self.denominator}'

    def fl(self):
        return self.__numerator/self.__denominator

    def __add__(self, another):
        """
        +
        """

        if not isinstance(another, Rational):
            raise TypeError('Invalid input data type')
        return Rational(self.numerator * another.denominator + self.denominator * another.numerator,
                        self.denominator * another.denominator) 

    def __sub__(self, another):
        """
        -
        """

        if not isinstance(another, Rational):
            raise TypeError('Invalid input data type')
        return Rational(self.numerator * another.denominator - self.denominator * another.numerator,
                        self.denominator * another.denominator)

    def __mul__(self, another):
        """
        *
        """

        if not isinstance(another, Rational):
            raise TypeError('Invalid input data type')
        return Rational(self.numerator * another.denominator, self.denominator * another.denominator)

    def __truediv__(self, another):
        """
        /
        """

        if not isinstance(another, Rational):
            raise TypeError('Invalid input data type')
        return Rational(self.numerator * another.denominator, self.denominator * another.numerator)

        # comparison operators

    def __eq__(self, another):
        """
        ==
        """

        if not isinstance(another, Rational):
            raise TypeError('Invalid input data type')
        return self.numerator / self.denominator == another.numerator / another.denominator

    def __ne__(self, another):
        """
        !=
        """

        if not isinstance(another, Rational):
            raise TypeError('Invalid input data type')
        return self.numerator / self.denominator != another.numerator / another.denominator

    def __gt__(self, another):
        """
        >
        """

        if not isinstance(another, Rational):
            raise TypeError('Invalid input data type')
        return self.numerator / self.denominator > another.numerator / another.denominator

    def __ge__(self, another):
        """
        >=
        """

        if not isinstance(another, Rational):
            raise TypeError('Invalid input data type')
        return self.numerator / self.denominator >= another.numerator / another.denominator

    def __lt__(self, another):
        """
        <
        """

        if not isinstance(another, Rational):
            raise TypeError('Invalid input data type')
        return self.numerator / self.denominator < another.numerator / another.denominator

    def __le__(self, another):
        """
        <=
        """

        if not isinstance(another, Rational):
            raise TypeError('Invalid input data type')
        return self.numerator / self.denominator <= another.numerator / another.denominator


try:
    r1 = Rational();
    r2 = Rational();
    print(f'addition: {r1 + r2} ')
    print(f'subtraction: {r1 - r2} ')
    print(f'multiplication: {r1 * r2} ')
    print(f'division: {r1 / r2} ')
except AttributeError:
    print("Wrong arguments")