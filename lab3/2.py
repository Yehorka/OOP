from json import load
from datetime import date
from enum import Enum
#class Pizzas(Enum):

class Pizza:
    def __init__(self):
        day = date.today().weekday()
        with open("pizza-of-the-day.json", "r") as f:
            data = load(f)
            self.ingredients = data[list(data)[day]]['ingredients']
            print(self.ingredients)
            self.day = list(data)[day]
    @property
    def day(self):
        return self.__day

    @property
    def ingredients(self):
        return self.__ingredients

    @day.setter
    def day(self, day):
        if not isinstance(day, str):
            raise TypeError("Must be list")
        self.__day = day

    @ingredients.setter
    def ingredients(self, ingredients):
        if not isinstance(ingredients, list):
            raise TypeError("Must be list")
        self.__ingredients = ingredients

    def __str__(self):
        with open("pizza-of-the-day.json", "r") as f:
            k = '|  ' + str(load(f)[self.day]['name']) + '\n'
        k += '-' * 25 + '\n'
        with open("ingredients.json", "r") as f:
            t = load(f)
        print()
        for i in self.ingredients:
            k += '| ' + i + '\n'
        return k

    def add_ingredients(self, ing):
        with open("ingredients.json", "r") as f:
            t = load(f)
        if self.ingredients.count(t[int(ing)]) > 0:
            self.ingredients.append("Extra " + t[int(ing)])
        else:
            self.ingredients.append(t[int(ing)])

    @staticmethod
    def show_ingredients():
        with open("ingredients.json", "r") as f:
            t = load(f)
        k = '|  ingredients\n' + '-' * 25 + ' \n'
        for i in range(len(t)):
            k += str(i) + '  -  ' + t[i] + ' \n'
        return k

try:
    p = Pizza()

    while True:
        print('Your pizza:\n' + str(p))
        t = input('Want to add something? If no - enter 0\n')
        if t == '0':
            break
        else:
            print(p.show_ingredients())
            p.add_ingredients(input('What did you want?\n'))
except:
    print("error")
