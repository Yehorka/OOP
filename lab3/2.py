from json import load
from json import dump
from datetime import date
from random import randint
PIZZA_JSON = "pizza-of-the-day.json"
INGREDIENTS_JSON = "ingredients.json"
ORDER_JSON = "order.json"
class Random_Pizza:
    def __init__(self):
        day = str(randint(0,6))
        with open(PIZZA_JSON, "r") as f:
            data = load(f)
            self.ingredients = data[day]['ingredients']
            self.day = day
    @property
    def day(self):
        return self.__day

    @property
    def ingredients(self):
        return self.__ingredients

    @day.setter
    def day(self, day):
        if not isinstance(day, str):
            raise TypeError("Must be str")
        self.__day = day

    @ingredients.setter
    def ingredients(self, ingredients):
        if not isinstance(ingredients, list):
            raise TypeError("Must be list")
        self.__ingredients = ingredients

    def __str__(self):
        with open(PIZZA_JSON, "r") as f:
            k = '|  ' + str(load(f)[self.day]['name']) + '\n'
        k += '-' * 25 + '\n'
        with open(INGREDIENTS_JSON, "r") as f:
            t = load(f)
        print()
        for i in self.ingredients:
            k += '| ' + i + '\n'
        return k

    def add_ingredients(self, ing):
        with open(INGREDIENTS_JSON, "r") as f:
            t = load(f)
        if self.ingredients.count(t[int(ing)]) > 0:
            self.ingredients.append("Extra " + t[int(ing)])
        else:
            self.ingredients.append(t[int(ing)])

    @staticmethod
    def show_ingredients():
        with open(INGREDIENTS_JSON, "r") as f:
            t = load(f)
        k = '|  ingredients\n' + '-' * 25 + ' \n'
        for i in range(len(t)):
            k += str(i) + '  -  ' + t[i] + ' \n'
        return k
    def form_order(self):
        with open(PIZZA_JSON, "r") as f:
            data = load(f)
            dumped = data[self.day]
            dumped['ingredients'] = self.ingredients
            dumped['date'] = str(date.today())
        with open(ORDER_JSON, 'w') as f:
            dump(dumped, f, indent = 4)


class Pizza_of_the_day(Random_Pizza):
    def __init__(self):
        super().__init__()
        with open(PIZZA_JSON, "r") as f:
            self.day = str(date.today().weekday())
try:
    p = Pizza_of_the_day()

    while True:
        print('Your pizza:\n' + str(p))
        t = input('Want to add something? If no - enter 0 to save your order\n')
        if t == '0':
            break
        else:
            print(p.show_ingredients())
            p.add_ingredients(input('What did you want?\n'))
            p.form_order()
except:
    print("error")
