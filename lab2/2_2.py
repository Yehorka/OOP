from re import split
from os.path import exists
class Texthandler:
    def __init__(self, name):
        if not exists(name):
            raise FileNotFoundError("No such file")
        file = open(name)
        self.__text = file.read()
        self.__characters = 0
        self.__words = 0
    def handle_words(self):
        print(self.__text)
        return len(self.__text.split())
    def handle_chars(self):
        return len(self.__text)
    def handle_sentences(self):
        res = split(r"[.?!\n]+", self.__text)
        return len(list(filter(lambda x: x, res)))
    def count_special_character(self, symbol):
        return self.__text.count(symbol)
text = Texthandler("F:/test.txt")
print(text.handle_words())
print(text.handle_sentences())
print(text.count_special_character(','))
