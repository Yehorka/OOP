from re import compile
class Queue:
    def __init__(self, *workers):
        self.workers = workers
    @property
    def workers(self):
        return self.__workers

    @workers.setter
    def workers(self, workers_list):
        if not workers_list:
            raise ValueError('Queue can`t be empty')
        if len(workers_list) > 20:
            raise ValueError('Queue must contain less than 20 workers')
        if not all(isinstance(item, Worker) for item in workers_list):
            raise TypeError('Workers must be worker type')
        self.__workers = list(workers_list)

    def add_worker(self, worker):
        if not isinstance(worker, Worker):
            raise TypeError("Workers must be Worker type")
        self.__workers.append(worker)

    def del_worker(self, worker):
        if not isinstance(worker, Worker):
            raise TypeError("Workers must be Worker type")
        self.__workers.remove(worker)

    def stats_most_expected_salary(self):
        self.workers.sort(key=lambda x: x.exp_sal, reverse=True)
        return (self.workers[:5])

    def stats_average_expected_salary(self):
        sum = 0
        for i in self.workers:
            sum += i.exp_sal
        average_score = round(sum / len(self.workers), 1)
        return average_score

class Worker:
    def __init__(self, surname, passport, education, job, date, exp_job, exp_sal):
        self.surname = surname
        self.passport = passport
        self.education = education
        self.job = job
        self.date = date
        self.exp_job = exp_job
        self.exp_sal = exp_sal

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be str")
        if not value:
            raise ValueError("Surname can`t be empty")
        self.__surname = value

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, value):
        if not isinstance(value, int):
            raise TypeError("Must be int")
        if not 0 <= value:
            raise ValueError("passport code must be higher than 0")
        self.__passport = value

    @property
    def education(self):
        return self.__education

    @education.setter
    def education(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be str")
        if not value:
            raise ValueError("education mustn`t be empty")
        self.__education = value

    @property
    def education(self):
        return self.__education

    @education.setter
    def education(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be str")
        if not value:
            raise ValueError("education mustn`t be empty")
        self.__education = value

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be str")
        if not value:
            raise ValueError("job mustn`t be empty")
        self.__job = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be str")
        if not value:
            raise ValueError("date mustn`t be empty")
        pattern = compile("^[0-3]?[0-9].[0-3]?[0-9].(?:[0-9]{2})?[0-9]{2}$")
        if not pattern.match(value): raise TypeError("Must be date */*/**")
        self.__date = value

    @property
    def exp_job(self):
        return self.__exp_job

    @exp_job.setter
    def exp_job(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be str")
        if not value:
            raise ValueError("exp_job mustn`t be empty")
        self.__exp_job = value

    @property
    def exp_sal(self):
        return self.__exp_sal

    @exp_sal.setter
    def exp_sal(self, value):
        if not isinstance(value, int):
            raise TypeError("Must be int")
        if not value:
            raise ValueError("exp_sal mustn`t be empty")
        self.__exp_sal = value

    def __str__(self) -> str:
        return f'{self.surname} {self.passport} {self.education} {self.job} {self.date} {self.exp_job} {self.exp_sal}'

    def __repr__(self):
        return str(self)
a = Worker("Suhulov", 228, "KPI", "waiter", "12/02/22", "programmer", 100000)
b = Worker("Ivanov", 128, "KNU", "waiter", "22/02/22", "Judge", 1000000)
print(a)
print(b)
e = Queue(a, b)
print
print(e.stats_most_expected_salary())
print(e.stats_average_expected_salary())