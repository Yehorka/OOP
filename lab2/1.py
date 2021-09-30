class Rectangle:
    def __init__ (self, width = 1.0, length = 1.0):
        self.__width = width
        self.__length = length
    def perimeter(self):
        return (self.__width + self.__length)*2
    def area(self):
        return (self.__width * self.__length)
    def set(self, width, length):
        if not isinstance(width, float) or not (isinstance(length, float)):
            raise TypeError
        if not((0. < width < 20. ) and (0. < length < 20.)):
            raise ValueError
        self.__width = width
        self.__length = length
    def get_length(self):
        return self.__length
    def get_width(self):
        return self.__width
r = Rectangle()
r.set(1., 19.0)
print(r.get_width())
print(r.area())
print(r.perimeter())
