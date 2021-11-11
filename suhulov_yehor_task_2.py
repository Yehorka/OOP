class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        if not isinstance(value, int):
            raise TypeError("Must be int")
        if not 0 <= value < 24:
            raise ValueError("hours must be higher than 0 and less than 24")
        self.__hours = value
    @property
    def minutes(self):
        return self.__minutes
    @minutes.setter
    def minutes(self, value):
        if not isinstance(value, int):
            raise TypeError("Must be int value!")
        if not 0 <= value < 60:
            raise ValueError("Minutes must be higher than 0 and less than 60")
        self.__minutes = value

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value):
        if not isinstance(value, int):
            raise TypeError("Must be int value!")
        if not 0 <= value < 60:
            raise ValueError("Seconds must be higher than 0 and less than 60")
        self.__seconds = value
    def increase(self):
        seconds = self.seconds + 1
        minutes = self.minutes + 1
        hours = self.hours + 1
        if seconds > 59:
            seconds -= 59
            minutes += 1
        if minutes > 59:
            minutes -= 59
            hours += 1
        if hours > 23:
            hours -= 24
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
    def __str__(self) -> str:
        return f'{self.__hours}:{self.__minutes}:{self.seconds}'
p = Time(23, 59, 10)
print(p)
p.increase()
print(p)