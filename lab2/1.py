class Rectangle:
    def __init__ (self, width = 1.0, length = 1.0):
        self.__width = width
        self.__length = length
    def perimeter(self):
        return (self.__width + self.__length)*2
    def area(self):
        return (self.__width * self.__length)
    def set(self, width, length):
        try:
            if (type(width) != float or type(length) != float):
                raise TypeError
            if (0. < width < 20. ) and (0. < length < 20.):
                self.__width = width
                self.__length = length
            else:
                print("Width and length shoule be smaller than 20 and greater than 0")
        except TypeError:
            print("Width and length should be float value")
    def get_length(self):
        return self.__length
    def get_width(self):
        return self.__width
r = Rectangle()
r.set(1., 19.0)
print(r.get_width())
print(r.area())
