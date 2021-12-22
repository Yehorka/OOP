from abc import abstractmethod, ABC

import jsonschema
from jsonschema import validate
import json

COURSE_JSON = "Course.json"
TEACHER_JSON = "Teacher.json"
COURSE_SCHEMA = "Course_schema.json"
TEACHER_SCHEMA = "Teacher_schema.json"


class ICourse(ABC):

    @abstractmethod
    def serialize(self, course_type):
        pass

    @abstractmethod
    def out_of_json(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @property
    @abstractmethod
    def course_program(self):
        pass


class ITeacher(ABC):

    @abstractmethod
    def serialize(self):
        pass

    @abstractmethod
    def add_course(self, name: str):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def courses(self):
        pass


class ILocalCourse(ABC):

    @abstractmethod
    def __str__(self): pass


class IOffsiteCourse(ABC):

    @abstractmethod
    def __str__(self): pass


class ICourseFactory(ABC):

    @abstractmethod
    def course_factory(self, name: str, course_program: list, course_type: str, teacher: ITeacher):
        pass

    @abstractmethod
    def teacher_factory(self, name: str):
        pass

    @abstractmethod
    def delete_course(self, course: ICourse):
        pass


class Course(ICourse):

    def __init__(self, name, course_program, teacher):
        self.name = name
        self.course_program = course_program
        self.teacher = teacher

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not value.rstrip():
            raise ValueError
        self.__name = value

    @property
    def course_program(self):
        return self.__course_program

    @course_program.setter
    def course_program(self, value):
        if not isinstance(value, list):
            raise TypeError
        if not all(isinstance(t, str) for t in value):
            raise ValueError
        self.__course_program = value

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, Teacher):
            raise TypeError
        self.__teacher = value

    def serialize(self, course_type):
        exists = False
        a = dict()
        with open(COURSE_JSON, "r") as f:
            data = json.load(f)
        for t in data:
            if t["name"] == self.name and t["teacher"] == self.teacher.name:
                exists = True
                break
        if exists:
            t["type"] = course_type
            t["program"] = self.course_program
            t["teacher"] = self.teacher.name
        else:
            a["name"] = self.name
            a["type"] = course_type
            a["program"] = self.course_program
            a["teacher"] = self.teacher.name
            data.append(a)
        self.put_to_json(data)

    @staticmethod
    def put_to_json(data):
        with open(COURSE_JSON, "w") as t:
            with open(COURSE_SCHEMA, "r") as schem:
                try:
                    schema = json.load(schem)
                    for part in data:
                        validate(part, schema)
                    json.dump(data, t, indent=4)
                except jsonschema.exceptions.ValidationError as err:
                    print(err)

    def out_of_json(self):
        with open(COURSE_JSON, "r") as f:
            data = json.load(f)
            for t in data:
                if t["name"] == self.name:
                    json.pop(t)
        with open(COURSE_JSON, "w") as f:
            json.dump(data, f, indent=4)

    def __str__(self) -> str:
        return f'Course:' \
               f'\n\tname - {self.__name}' \
               f'\n\tteacher - {self.__teacher.name}' \
               f'\n\tprogram - {self.__course_program}'

class Teacher(ITeacher):

    def __init__(self, name):
        self.name = name
        self.courses = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not value.rstrip():
            raise ValueError
        self.__name = value

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        if not isinstance(value, list):
            raise TypeError
        self.__courses = value

    def add_course(self, name : str):
        if name in self.courses:
            pass
        else:
            self.courses.append(name)

    def serialize(self):
        exists = False
        with open(TEACHER_JSON, "r") as f:
            data = json.load(f)
        for teacher in data:
            if teacher["name"] == self.name:
                exists = True
                break
        if exists:
            teacher["courses"] = self.courses
        else:
            a["name"] = self.name
            a["courses"] = self.courses
            data.append(a)
        self.put_to_json(data)


    @staticmethod
    def put_to_json(data):
        with open(TEACHER_JSON, "w") as t:
            with open(TEACHER_SCHEMA, "r") as schem:
                try:
                    schema = json.load(schem)
                    for part in data:
                        validate(part, schema)
                    json.dump(data, t, indent=4)
                except jsonschema.exceptions.ValidationError as err:
                    print(err)

    def __str__(self):
        return f'Teacher:' \
               f'\n\tname - {self.__name}' \
               f'\n\tcourses - {self.__courses}'

class LocalCourse(Course, ILocalCourse):

    def __init__(self, name, program, teacher):
        super().__init__(name, program, teacher)
        super().serialize("local")

    def delete(self):
        super().out_of_json()

    def __str__(self) -> str:
        return super().__str__() + \
               f'\n\tLocal'

class OffsiteCourse(Course, IOffsiteCourse):

    def __init__(self, name, program, teacher):
        super().__init__(name, program, teacher)
        super().serialize("offset")

    def delete(self):
        super().out_of_json()

    def __str__(self) -> str:
        return super().__str__() + \
               f'\n\toffset'

class CourseFactory(ICourseFactory):

    def course_factory(self, name: str, course_program: list, course_type: str, teacher: ITeacher):
        if course_type == 'local':
            a = LocalCourse(name, course_program, teacher)
        elif course_type == 'offset':
            a = OffsiteCourse(name, course_program, teacher)
        else:
            raise ValueError("Wrong")
        teacher.add_course(name)
        teacher.serialize()
        return a

    def teacher_factory(self, name):
        with open(TEACHER_JSON, "r") as file_teacher:
            teachers = json.load(file_teacher)
            for t in teachers:
                if name == t["name"]:
                    teacher = Teacher(t["name"])
                    teacher.courses.extend(t["courses"])
                    return teacher
                else:
                    return Teacher(name)

    def delete_course(self, course):
        course.out_of_json()



f = CourseFactory()
t = f.teacher_factory("Andrii")
d = f.teacher_factory("Danylo")
a = f.course_factory("Test", ["damn", "yeah"], "local", t)
b = f.course_factory("Test", ["damn", "yeah", "it works!"], "offset", t)
print(a)