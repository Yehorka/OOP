# The class GROUP contains a sequence
# of instances of the class STUDENT.
# The class STUDENT contains the
# student's name, surname, record book number
# and grades.
# Determine the required attributes-data
# and attributes-methods in classes GROUP and STUDENT.
# Find the average score of each student.
# Output to the standard output stream the five
# students with the highest average score.
# Assume that there can be no more than 20 students
# in a group, as well as students with
# the same name and surname.
class Student:
    def __init__(self, name, surname, record_book, *grades):
        self.name = name
        self.surname = surname
        self.record_book = record_book
        self.grades = grades

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('surname has to be a string variable')
        if name == '':
            raise ValueError('name shouldn`t be empty!')
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError('surname has to be a string variable')
        if surname == '':
            raise ValueError('surname shouldn`t be empty!')
        self.__surname = surname

    @property
    def record_book(self):
        return self.__record_book

    @record_book.setter
    def record_book(self, record_book):
        if not isinstance(record_book, int):
            raise TypeError('record book number must be Int')
        self.__record_book = record_book

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        if not all(isinstance(i, int) for i in grades):
            raise TypeError('Grade must be Int')
        if not grades:
            raise ValueError('Shouldn`t be empty')
        self.__grades = grades
        self.__average_score = round(sum(grades) / len(grades), 1)

    @property
    def average_score(self):
        return self.__average_score
    def __str__(self) -> str:
        return f'name: {self.name}\nsurname: {self.surname}\nRecord book number: {str(self.record_book)}\nGrades: {self.grades}\nAverage: {self.average_score}'
class Group:
    def __init__(self, *students):
        self.students = students

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, student_list):
        if not student_list:
            raise ValueError('Group can`t be empty')
        if len(student_list) > 20:
            raise ValueError('Group must contain less than 20 students')
        if isinstance(all(student_list), Student):
            raise TypeError('Students must be Student type')
        if self.__hasDuplicates(student_list):
            raise ValueError('Group can`t have students with same surname and name')
        self.__students = list(student_list)
    def best(self):
        self.students.sort(key=lambda x: x.average_score, reverse=True)

    def __hasDuplicates(self, student_list):
        counter = 0
        names = set()
        for i in student_list:
            names.add(i.name + i.surname)
            counter += 1
        if counter > len(names):
            return True
        return False
    def __str__(self):
        st = ""
        for i in self.students[:5]:
            st += str(i) + "\n"
        return f'{st}'

example1 = Student('Suhulov', 'Yehor', 3, 3,5,3,3,2,4)
example2 = Student('Suhulova', 'Yehor', 3, 4,5,3,3,2,4)
example3 = Student('Suhulovb', 'Yehor', 3, 5,5,3,3,2,4)
example4 = Student('Suhulovc', 'Yehor', 3, 6,5,3,3,2,4)
example5 = Student('Suhulovd', 'Yehor', 3, 7,5,3,3,2,4)
example6 = Student('Suhulove', 'Yehor', 3, 8,5,3,3,2,4)
group = Group(example1, example2, example3, example4, example5, example6)
group.best()
print(group)
#print(example1)
