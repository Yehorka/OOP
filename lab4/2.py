import re
import json

class Birthday:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not isinstance(day, int):
            raise TypeError("Day must be integer!")
        if not 0 < day <= 31:
            raise ValueError("The day has to be between 1 and 31 (inclusive)!")
        self.__day = day

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise TypeError("Month must be integer!")
        if not 0 < month <= 12:
            raise ValueError("The month has to be between 1 and 12 (inclusive)!")
        self.__month = month

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError("Year must be integer!")
        if not 0 < year <= 2021:
            raise ValueError("The year has to be between 1 and 2021 (inclusive)!\n(Unfortunately I don't care about "
                             "very old years.....)")
        self.__year = year
    def __repr__(self):
        return f"Birthday:\n\t\tThe day: {self.day}\n" \
               f"\t\tThe month: {self.month}\n" \
               f"\t\tThe year: {self.year}"
    def __str(self):
        return f"Birthday:\n\t\tThe day: {self.day}\n" \
               f"\t\tThe month: {self.month}\n" \
               f"\t\tThe year: {self.year}"


class Note:
    def __init__(self, name, surname, phone_number, birthday):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.birthday = birthday

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be string!")
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Surname must be string!")
        self.__surname = surname

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        if not re.fullmatch(r'\+380\d{9}', phone_number):
            raise TypeError("Phone number must follow this example!\n+380xxxxxxxxx")
        self.__phone_number = phone_number

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        if not isinstance(birthday, Birthday):
            raise TypeError("The birthday must be instance of the class 'Birthday'!")
        self.__birthday = birthday

    def __str__(self):
        return f"INFO:\n\tThe name: {self.name}\n" \
               f"\tThe surname: {self.surname}\n" \
               f"\tPhone number: {self.phone_number}\n" \
               f"\tBirthday: {self.birthday}\n"

class Notebook:
    def __init__(self):
        self.all_records = []

    def __add__(self, other):
        if not isinstance(other, Note):
            raise TypeError("The record must be instance of class 'Note'!")
        self.all_records.append(other)

    def __sub__(self, other):
        for record in self.all_records:
            if record.name == other:
                self.__all_records.remove(record)

    def __mul__(self, other):
        for record in self.all_records:
            if record.name == other:
                return record

    def __str__(self):
        if len(self.all_records):
            return "\n".join(map(str, self.__all_records))
        return "\t\t (EMPTY)\n"
    
notebook = Notebook()
notebook + Note("Yehor", "Suhulov", "+380963268933", Birthday(18,11,2002))
notebook + Note("Myhailo", "Lahoida", "+380678876588", Birthday(30,8,2003))
notebook + Note("Danylo", "Grinchishin", "+380452063821", Birthday(11,4,2002))

print("There is notebook. What would you like to do?")
while True:
    print("1. Add new element (record)")
    print("2. Delete particular element (record)")
    print("3. Search particular element (record)")
    print("4. Quit (and show all notes)")
    answer1 = input()
    while answer1 not in "1234":
        print("Incorrect input!Type again")
        answer1 = input()
    if answer1 == '4':
        print("\t\tWHOLE LIST\n")
        print(notebook)
        print("Finishing the work...")
        break
    if answer1 == '1':
        print("Print: (Use enter after all printed answers!!!)")
        notebook + Note(input("\nThe name\n"), input("\nSurname\n"),
                            input("\nPhone number (like this +380xxxxxxxxx)\n"),
                            Birthday(int(input("\nBirthday:\n\tthe day\n\t")), int(input("\n\tthe month\n\t")),
                                     int(input("\n\tthe year\n\t"))))
    if answer1 == '2':
        notebook - input("Name for delete the record\n(Be attentive!You'll delete ALL records with this name!!)\n")
    if answer1 == '3':
        print("Print:\n\t")
        print(notebook * input("Name for search the first record with this name\n"))