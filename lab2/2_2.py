from re import split, sub, VERBOSE
from os.path import exists


class Texthandler:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Must be str")
        if name == "":
            raise NameError("Name is empty")
        if not exists(name):
            raise FileNotFoundError("No such text")

        self.__filename = name

    def handle(self):
        file = open(self.__filename)
        chars = 0
        words = 0
        sent = 0
        for line in file:
            line = line.strip("\n")
            chars += len(line)
            res = split(r"[.?!\n]+", line)
            line.replace(r"[,?.;]+", ' ')
            clean = sub(r"""[,.;@#?!&$]+\ *,"""," ",line, flags = VERBOSE)
            word = clean.split()
            words += len(word)
            sent = len(list(filter(lambda x: x, res)))
        file.close()
        return chars, words, sent


    def __str__(self) -> str:
        text = self.handle()
        return f'Stats:\nChars:{text[0]}\nWords:{text[1]}\nSentences:{text[2]}'


text = Texthandler("test.txt")
print(text)
