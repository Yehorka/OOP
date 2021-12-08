from math import gcd

class Rational:
    def __init__(self, numerator=2, denominator=4):
        self.denominator = denominator
        self.numerator = numerator
        self.reduct()
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

    def reduct(fnc):
        def inner(self, other):
            self = fnc(self, other)
            tmp = gcd(self.numerator, self.denominator)
            self.numerator //= tmp
            self.denominator //= tmp
            return self
        return inner
    def __str__(self) -> str:
        return f'{self.numerator}/{self.denominator}'
    def __repr__(self):
        return f'{self.numerator}/{self.denominator}'

    def fl(self):
        return self.__numerator/self.__denominator
    @reduct
    def __iadd__(self, other):
        """
         +=
        """

        if not isinstance(other, (Rational, int)):
            return NotImplemented

        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator + self.denominator * other.numerator
            self.denominator = self.denominator * other.denominator
        else:
            self.numerator = self.numerator + self.denominator * other

        return self

    @reduct
    def __isub__(self, other):
        """
        -=
        """

        if not isinstance(other, (Rational, int)):
            return NotImplemented

        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator - self.denominator * other.numerator
            self.denominator = self.denominator * other.denominator
        else:
            self.numerator = self.numerator + self.denominator * other
        return self

    @reduct
    def __add__(self, other):
        """
        +
        """

        if not isinstance(other, Rational):
            return NotImplemented
        self.numerator = self.numerator * other.denominator + self.denominator * other.numerator
        self.denominator = self.denominator * other.denominator
        return self

    @reduct
    def __sub__(self, other):
        """
        -
        """

        if not isinstance(other, Rational):
            return NotImplemented
        self.numerator = self.numerator * other.denominator - self.denominator * other.numerator
        self.denominator = self.denominator * other.denominator
        return self

    @reduct
    def __mul__(self, other):
        """
        *
        """

        if not isinstance(other, Rational):
            return NotImplemented
        self.numerator = self.numerator * other.numerator
        self.denominator = self.denominator * other.denominator
        return self

    @reduct
    def __truediv__(self, other):
        """
        /
        """

        if not isinstance(other, Rational):
            return NotImplemented
        self.numerator = self.numerator * other.denominator
        self.denominator = self.denominator * other.numerator
        return self

        # comparison operators

    def __eq__(self, other):
        """
        ==
        """

        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator / self.denominator == other.numerator / other.denominator

    def __ne__(self, other):
        """
        !=
        """

        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator / self.denominator != other.numerator / other.denominator

    def __gt__(self, other):
        """
        >
        """

        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator / self.denominator > other.numerator / other.denominator

    def __ge__(self, other):
        """
        >=
        """

        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator / self.denominator >= other.numerator / other.denominator

    def __lt__(self, other):
        """
        <
        """

        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator / self.denominator < other.numerator / other.denominator

    def __le__(self, other):
        """
        <=
        """

        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator / self.denominator <= other.numerator / other.denominator


try:
    r1 = Rational();
    r2 = Rational();
    print(f'addition: {r1 + r2} ')
    print(f'subtraction: {r1 - r2} ')
    print(f'multiplication: {r1 * r2} ')
    print(f'division: {r1 / r2} ')
    r1 += r2
    print(f'{r1}+={r2} : {r1}')
    r1 -= r2
    print(f'{r1}-={r2} : {r1}')
    print(f'{r1}>{r2}: {r1 > r2}')
    print(f'{r1}>={r2}: {r1 >= r2}')
    print(f'{r1}<{r2}: {r1 < r2}')
    print(f'{r1}<={r2}: {r1 <= r2}')
    print(f'{r1}=={r2}: {r1 == r2}')
    print(f'{r1}!={r2}: {r1 != r2}')
except AttributeError:
    print("Wrong arguments")